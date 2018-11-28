#include<bits/stdc++.h>
using namespace std;

int main()
{
  int t;
  string s;

  cin>>t;
  for(int i=0;i<t;i++){
    cin>>s;

    vector<int> st;

    for(int j=0;j<s.length();j++){
      if(s[j]=='+')st.push_back(1);
      else st.push_back(0);
    }

    int count=0;


    while(!st.empty()){
      /*  for(int i=0;i<st.size();i++)cout<<st[i]<<" ";
	  cout<<endl;*/

      int a=st.back();
      st.pop_back();

      if(a==1)continue;
      vector<int> st2;
      while(!st.empty()){
	st2.push_back((st.back()+1)%2);
	st.pop_back();
      }

      while(!st2.empty()){
	st.push_back(st2.back());
	st2.pop_back();
      }
      st.push_back(1);
      count++;

    }
    printf("Case #%d: %d\n",i+1,count);
  }

  return 0;
}
