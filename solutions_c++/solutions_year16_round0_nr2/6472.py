#include<string.h>
#include<stdio.h>
//#include<fstream>

using namespace std;

int main()
{
	int N,T = 0,L,ans;
//	ofstream cout("1.txt");
	char k[107];
	scanf("%d",&N);
	while(N--){
		ans = 0;
		scanf("%s",k);
		L = strlen(k);
		for(int i = 1;i < L ;i++)
			if(k[i]!=k[i-1]) ans++;
		if(k[L-1]=='-') ans++;
		printf("Case #%d: %d\n",++T,ans);
	//	cout<<"Case #"<<T<<": "<<ans<<"\n";
	} 
	return 0;
}
