#include <bits/stdc++.h>

using namespace std;

vector<int> cakes;

void printCakes(){
	for(int i=0;i<cakes.size();i++){
		printf("%d ",cakes[i]);
	}
	printf("\n");
}

int minMinutes(){
	//printCakes();
	int x=*max_element(cakes.begin(),cakes.end());
	if(x<=2) return x;
	for(int i=0;i<cakes.size();i++){
		cakes[i]--;
	}
	int res=1+minMinutes();
	for(int i=0;i<cakes.size();i++){
		cakes[i]++;
	}
	int ind=max_element(cakes.begin(),cakes.end())-cakes.begin();
	for(int i=x/2;i>=(x/2)-1 && i>=1;i--){
		cakes[ind]=i;
		cakes.push_back(x-i);
		res=min(res,1+minMinutes());
		cakes[ind]=x;
		cakes.pop_back();
	}
	/*cakes[ind]=x/2;
	cakes.push_back(x-(x/2));
	res=min(res,1+minMinutes());
	cakes.pop_back();
	cakes[ind]=x;*/
	return res;
}

int main(int argc, char const *argv[]){

	//freopen("C:\\Users\\Toshiba\\Desktop\\B-small-attempt4.in","r",stdin);
	//freopen("C:\\Users\\Toshiba\\Desktop\\output.txt","w",stdout);
	
	int tt,t,d,tmp;
	scanf("%d",&tt);

	for(t=0;t<tt;t++){

		cakes.clear();

		scanf("%d",&d);
		for(int i=0;i<d;i++){
			scanf("%d",&tmp);
			cakes.push_back(tmp);
		}

		printf("Case #%d: %d\n",t+1,minMinutes());

	}

	return 0;
}