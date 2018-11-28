#include <iostream>
#include <string>
#include <vector>
using namespace std;
//const char* FILE_IN = "test.in";
const char* FILE_IN = "C-small-attempt0.in";
const char* FILE_OU = "C-small-attempt0.ou";

int cnt;
int A,B;

void buildNumber ( int len, string a , int size) {
	if ( len==size/2+1 ) {
		//special case when size = 2
		if ( size == 2 ) {
			if ( a[0]!=a[1] ) return;
		}
		string s(size,' ');
		for ( int i=0 ; i<len ; i++ ) {
			s[i] = a[i];
		}
		
		if ( size%2 ) {
			for (int i = 0; i < size-len; i++) {
				s[len+i] = s[len-i-2];
			}
		}
		else {
			for (int i = 0; i < size-len; i++) {
				s[len+i] = s[len-i-1];
			}
		}
		int ia = atoi(s.c_str());
		char str_buff[128];
		sprintf(str_buff,"%d",ia*ia);
		//cout<<str_buff<<endl;
		//check pa
		int n = strlen(str_buff);
		int i;
		for ( i=0 ; i<n/2 ; i++ ) {
			if ( str_buff[i]!=str_buff[n-1-i] ) break;
		}
		if ( i==n/2 ) {
			ia = atoi(str_buff);
			if ( i==n/2 && ia>=A && ia<=B ) {
				//cout<<ia<<endl;
				cnt++;
			}
		}
		return ;
	}
	
	for ( char c='0' ; c<='9' ; c++ ) {
		if ( c=='0' && len==0 ) continue;
		buildNumber(len+1,a+c,size);
	}
}
int calcLen ( int a ) {
	int ret= 1;
	while ( a/=10 ) ret++;
	return ret;
}
int main ( ) {
	int cas;
	freopen(FILE_IN,"r",stdin);
	freopen(FILE_OU,"w",stdout);
	cin>>cas;
	for ( int i=1 ; i<=cas; i++ ) {
		cout<<"Case #"<<i<<": ";
		cnt=0;
		cin>>A>>B;
		int la = calcLen((int)sqrt(1.0*A));
		int lb = calcLen((int)sqrt(1.0*B));
		for ( int j=la ; j<=lb ; j++ ) {
			buildNumber (0,"",j);
		}
		cout<<cnt<<endl;
	}
	return 0;

}