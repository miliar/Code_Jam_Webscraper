# include <stdio.h>
# include <stdlib.h>
# include <cstdlib>
# include <iostream>
# include <cstdio>
# include <string>
# include <cstring>
# include <sstream>
# include <math.h>
# include <algorithm>

using namespace std;

int fn(string s, int n){
int i,j,k,l,m,mm,ans=0;
l = s.length();
//cout << s << l << endl;
for(i = 0 ; i < l ; i++){
for(j = i ; j < l ; j++){
//cout << i << ":" << j << " -";
mm = 0;
for(k = i,m=0; k <= j ; k++){
if((s[k]=='a')||(s[k]=='e')||(s[k]=='i')||(s[k]=='o')||(s[k]=='u')){
mm=((mm<m)?m:mm);
m=0;
}
else{
++m;
mm=((mm<m)?m:mm);
}
//cout << mm << endl;
}

if(mm>=n){
ans++;
}
//cout << ans << endl;
}
//break;
}
return ans;
}


int main(void){
	int i,j,k,l,cases_no,m,n;
	string s;
cin >>cases_no;
for(i = 1 ; i <= cases_no ; i++){
cin >> s >> n;
cout << "Case #" << i << ": " << fn(s, n) << endl;
}
return 0;
}
