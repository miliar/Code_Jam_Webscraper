#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <cmath>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
int rev(int x){
    int r=0;

while(x>0)
{
r=r*10;
r=r+x%10;
x=x/10;
}
return r;
}
bool plain(int x){
   if((x==rev(x))&&(sqrt(x)==rev(sqrt(x))))
    return 1;
    return 0;
}
int solve(int n,int m){
int cnt=0;
for(int i=n;i<=m;i++)
if(plain(i))cnt++;
return cnt;
}
int main(){
	READ("C-small-attempt0.in");
	WRITE("C-large-1.out");
	int tries,m,n;
	cin>>tries;
	for(int i=1;i<=tries;i++){
	    cin>>n>>m;
		cout<<"Case #"<<i<<": "<<solve(n,m)<<endl;
	}
	return 0;
}
