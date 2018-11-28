#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

typedef long long in;

using namespace std;

int main(){
  in t;
  cin >> t;
  for(in test=1;test<=t;test++){
    in n;
    cin >> n;
    vector<in> m;
    m.resize(n);
    for(in i=0;i<n;i++)
      cin >> m[i];
    in x=0;
    in y=0;
    in rate=0;
    for(in i=0;i<n-1;i++){
      if(rate<(m[i]-m[i+1]))
	rate=m[i]-m[i+1];
    }
    for(in i=0;i<n-1;i++){
      if(m[i]>m[i+1])
	x+=(m[i]-m[i+1]);
      if(m[i]>=m[i+1]){
	if(m[i]-rate<0)
	  y+=m[i];
	else
	  y+=rate;
      }
      if(m[i+1]>m[i]){
	   if(m[i]-rate<=0){
	    y+=m[i];
	  }
	  else{
	    y+=rate;
	  }
	}
      }
    cout << "Case #" << test << ": " << x << " " << y << endl;
  }
  return 0;
}
  
      