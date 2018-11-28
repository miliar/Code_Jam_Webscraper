#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>


#define maxn 1010
#define deb printf

using namespace std;
char a[maxn];
int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%s",a);
		int len=strlen(a);
		string b="";
		b=a[0];
		for(int j=1;j<len;j++){
			if(b[0]<=a[j])b=a[j]+b;
			else b=b+a[j];
		}
		printf("Case #%d: %s\n",i+1,b.c_str());
	}


	return 0;
}