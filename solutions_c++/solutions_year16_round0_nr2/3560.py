#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include<set>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
	int tc;cin>>tc;
	for(int j=1;j<=tc;j++){
	        string str;cin>>str;
	        if(str.length()==1){
	                if(str[0]=='+') cout<<"Case #"<<j<<": 0\n";
	                else cout<<"Case #"<<j<<": 1\n";
	        }
	        else{
	                reverse(str.begin(), str.end());
	                int chk1=0,chk2=0,ans=0;
	                for(int i=1;i<str.length();i++){
	                        if(str[i]==str[i-1]) continue;
	                        if(str[i]=='-' && str[i-1]=='+') ans++;
	                        if(str[i]=='+' && str[i-1]=='-') ans++;
	                }
	                for(int i=1;i<str.length();i++){
	                        if(str[i]==str[i-1]) continue;
	                        if(str[i]=='+' && str[i-1]=='-'){
	                                chk1=1;
	                                break;
	                        }
	                        if(str[i]=='-' && str[i-1]=='+'){
	                                chk2=1;
	                                break;
	                        }
	                }
	                
	                if(chk1==1) cout<<"Case #"<<j<<": "<<ans+1<<endl;
	                else if(chk2==1) cout<<"Case #"<<j<<": "<<ans<<endl;
	                else{
	                        int count0=0,count1=0;
	                        for(int i=0;i<str.length();i++)
	                                if(str[i]=='-') count0++;
	                                else count1++;
	                         if(count0==0) cout<<"Case #"<<j<<": 0\n";
	                         else cout<<"Case #"<<j<<": 1\n";
	                }
	        }
	}
	return 0;
}
