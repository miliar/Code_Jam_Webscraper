#include <stdio.h>
#include <string>
#include <sstream>

#define f(i,n) for(int i =0; i<n;i++)
using namespace std;

bool isPal(int a){
	string s;
	stringstream st;
	st<<a;
	s = st.str();
	f(i,s.length())
		if(s[i]!=s[s.length()-1-i])
			return false;
	return true;
}

int main(){
	int tc,a,b;
	scanf("%d",&tc);
	f(i,tc){
		scanf("%d %d",&a,&b);
		int num=0;
		for(int j=(int)sqrt(a);j<=(int)sqrt(b)+1;j++)
			if(((j*j)>b)||((j*j)<a))continue;
			else
				num+=isPal(j*j)&&isPal(j);
		printf("Case #%d: %d\n",i+1,num);
	}
	return 0;
}
