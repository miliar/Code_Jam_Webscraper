#include <cstdio>
#include <cmath>
#include <vector>

using namespace  std;

bool jp(int x)
{
	vector<int> v;
	while(x>0){
	v.push_back(x%10);
	x=x/10;
	}
	int i=0,j=v.size()-1;
	while(1){
		if(i==j || i-1==j) return true;
		if(v[i]!=v[j]) return false;
		i++; j--;
	}
}

int main()
{
	int n,kolo,a,b;
	scanf("%d",&n);
	int pole[1001]; for(int i=0;i<1001;i++) pole[i]=0;
	for(int i=1;i<40;i++){
		if(jp(i) && jp(i*i) && i*i<1001){  pole[i*i]=1;}
		else pole[i*i]=0;
	}
	//for(int i=0;i<1000;i++) if(pole[i]==1) printf("%d ",i); printf("\n");
	for(int i=0;i<n;i++){
		kolo=0;
		scanf("%d%d",&a,&b);
		for(int j=a;j<=b;j++){
			if(pole[j]==1) kolo++;
		}
		printf("Case #%d: %d\n",i+1,kolo);
	}
	return 0;
}

























