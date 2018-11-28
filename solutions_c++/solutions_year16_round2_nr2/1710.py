#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>

using namespace std;

typedef long long in;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int test=0;test<t;test++){
    string a,b;
    cin >> a >> b;
    vector<string> q;
    vector<string> m;
    bool flag=0;
    if(a.size()==3&&a[0]=='?'&&a[1]=='?'&&a[2]=='?'){
      for(int j=0;j<10;j++){
	for(int k=0;k<10;k++){
	  for(int s=0;s<10;s++){
	    a.replace(0,1,to_string(j));
	    a.replace(1,1,to_string(k));
	    a.replace(2,1,to_string(s));
	    q.push_back(a);
	  }
	}
      }
    }
    else if(a.size()>=2&&a[0]=='?'&&a[1]=='?'){
      for(int j=0;j<10;j++){
	for(int k=0;k<10;k++){
	  a.replace(0,1,to_string(j));
	  a.replace(1,1,to_string(k));
	  q.push_back(a);
	}
      }
    }
    else if(a.size()>=2&&a[0]=='?'&&a[2]=='?'){
      for(int j=0;j<10;j++){
	for(int k=0;k<10;k++){
	  a.replace(0,1,to_string(j));
	  a.replace(2,1,to_string(k));
	  q.push_back(a);
	}
      }
    }
    else if(a.size()>=2&&a[1]=='?'&&a[2]=='?'){
      for(int j=0;j<10;j++){
	for(int k=0;k<10;k++){
	  a.replace(1,1,to_string(j));
	  a.replace(2,1,to_string(k));
	  q.push_back(a);
	}
      }
    }
    else{
      for(int i=0;i<a.size();i++){
	if(a[i]=='?'){
	  flag=1;
	  for(int j=0;j<10;j++){
	    a.replace(i,1,to_string(j));
	    q.push_back(a);
	  }
	}
      }
      if(!flag)
	q.push_back(a);
    }
    flag=0;
    if(b.size()==3&&b[0]=='?'&&b[1]=='?'&&b[2]=='?'){
      for(int j=0;j<10;j++){
	for(int k=0;k<10;k++){
	  for(int s=0;s<10;s++){
	    b.replace(0,1,to_string(j));
	    b.replace(1,1,to_string(k));
	    b.replace(2,1,to_string(s));
	    m.push_back(b);
	  }
	}
      }
    }
    else if(b.size()>=2&&b[0]=='?'&&b[1]=='?'){
      for(int j=0;j<10;j++){
	for(int k=0;k<10;k++){
	  b.replace(0,1,to_string(j));
	  b.replace(1,1,to_string(k));
	  m.push_back(b);
	}
      }
    }
    else if(b.size()>=2&&b[0]=='?'&&b[2]=='?'){
      for(int j=0;j<10;j++){
	for(int k=0;k<10;k++){
	  b.replace(0,1,to_string(j));
	  b.replace(2,1,to_string(k));
	  m.push_back(b);
	}
      }
    }
    else if(b.size()>=2&&b[1]=='?'&&b[2]=='?'){
      for(int j=0;j<10;j++){
	for(int k=0;k<10;k++){
	  b.replace(1,1,to_string(j));
	  b.replace(2,1,to_string(k));
	  m.push_back(b);
	}
      }
    }
    else{
      for(int i=0;i<b.size();i++){
	if(b[i]=='?'){
	  flag=1;
	  for(int j=0;j<10;j++){
	    b.replace(i,1,to_string(j));
	    m.push_back(b);
	  }
	}
      }
      if(!flag)
	m.push_back(b);
    }
    int mini=1000;
    int minj=0;
    string c1,j1;
    for(int i=0;i<q.size();i++){
      for(int j=0;j<m.size();j++){
	int r=stoi(q[i]);
	int d=stoi(m[j]);
	if(abs(r-d)<mini){
	  mini=abs(r-d);
	  minj=d;
	  c1=q[i];
	  j1=m[j];
	}
	if(abs(r-d)==mini&&minj>d){
	  minj=d;
	  c1=q[i];
	  j1=m[j];
	}
      }
    }
    cout << "Case #" << test+1 << ": " << c1 << " " << j1 << endl;
  }
  return 0;
}