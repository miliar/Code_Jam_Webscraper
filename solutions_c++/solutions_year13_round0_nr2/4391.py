#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>

using namespace std;

FILE *fin;
FILE *fout;

int n,m;
int a[110][110];

struct Type{
	int num;
	int x;
	int y;
	bool operator<(Type t) const{
		if(num != t.num)
			return num < t.num;
		if(x != t.x)
			return x < t.x;
		return y < t.y;
	}
};

vector<Type> vec;
bool checked[110][110];
int main(){
	fin = fopen("B-large.in","r");
	fout = fopen("gcjout.txt","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int caseT = 1;caseT <= T;++caseT){
		vec.clear();
		fscanf(fin,"%d%d",&n,&m);
		for(int i = 1;i <= n;++i)
			for(int j = 1;j <= m;++j){
				fscanf(fin,"%d",&a[i][j]);
				Type t;
				t.x = i;
				t.y = j;
				t.num = a[i][j];
				vec.push_back(t);
			}
		sort(vec.begin(),vec.end());
		memset(checked,false,sizeof(checked));
		bool ok = true;
		for(int i = 0;i < vec.size();++i){
			Type now = vec[i];
			if(checked[now.x][now.y])
				continue;
			bool found = true,found2 = true;
			for(int i = 1;i <= n;++i){
				if(a[i][now.y] > a[now.x][now.y]){
					found = false;
					break;
				}
			}
			if(found){
				for(int i = 1;i <= n;++i)
					checked[i][now.y] = true;
			}else{
				for(int i = 1;i <= m;++i){
					if(a[now.x][i] > a[now.x][now.y]){
						found2 = false;
						break;
					}
				}
				if(found2){
					for(int i = 1;i <= m;++i)
						checked[now.x][i] = true;
				}
			}
			if(found == false && found2 == false){
				ok = false;
				break;
			}
		}
		fprintf(fout,"Case #%d: %s\n",caseT,ok ? "YES" : "NO");
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

