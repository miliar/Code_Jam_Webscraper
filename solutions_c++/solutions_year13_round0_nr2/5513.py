#include<stdio.h>
#include<iostream>
#include<queue>

typedef long long int ll;

using namespace std;

typedef struct _lawn{
	int x,y,val;
	_lawn(int _x,int _y,int _val):x(_x),y(_y),val(_val){}
}lawn;

class comp{
	public:
		bool operator() (const lawn &lhs,const lawn &rhs){
			return (lhs.val > rhs.val);
		}
};

int main(){

	priority_queue<lawn,vector<lawn>,comp> Q;	
	int test,n,m,arr[105][105],cnt=1;
	bool no,row[105],col[105],brow,bcol;
	scanf("%d",&test);
	while(test--){

		scanf("%d %d",&n,&m);

		for(int i=0;i<n;i++)
			row[i] = false;
		for(int i=0;i<m;i++)
			col[i] = false;
		 no = false;

		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				scanf("%d",&arr[i][j]);
				Q.push(lawn(i,j,arr[i][j]));
			}

		while(!Q.empty()){

			int x = Q.top().x;
			int y = Q.top().y;
			int val = Q.top().val;
			Q.pop();

			brow = bcol = true;
			if(row[x] == false){
				for(int i=0;i<m;i++)
					if(!col[i] && arr[x][i] != val)
					{
						brow=false;
						break;
					}
				if(brow != false)
					row[x] = true;
			}

			if(col[y] == false){
				for(int i=0;i<n;i++)
					if(!row[i] && arr[i][y] != val)
					{
						bcol=false;
						break;
					}
				if(bcol != false)
					col[y] = true;
			}

			if(brow == false && bcol == false){
				no = true;
				break;
			}

		}

		while(!Q.empty())
			Q.pop();
		if(no == true)
			printf("Case #%d: NO\n",cnt);
		else
			printf("Case #%d: YES\n",cnt);
		cnt++;

	}

	return 0;
}

