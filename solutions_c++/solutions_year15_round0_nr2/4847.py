#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

int ans[9];
//vector<int> q;
int solve(vector<int> p,int d,int ctr)
{
      vector<int> o,q;
      int r=100;
      // if(p[d]==4) return ctr+3;
      /*  cout<<" p[d] = "<<p[d]<<" d= "<<d<<" ctr = "<<ctr<<endl;
      for(int i=0;i<p.size();i++){
	     cout<<p[i]<<"\t";
	 }cout<<endl;*/
      if(p[d]==3) return ctr+3;
      else if(p[d]==2) return ctr+2;
      else if(p[d]==1) return ctr+1;
      else if(p[d]==0) return ctr+0;
      ctr++;
      sort(p.data(),p.data()+d+1);
      q=p;
      for(int i=0;i<p.size();i++){
	    q[i]=p[i]-1;

      }
      int k=p[d];
      o=p;
       for(int i=2;i<=k/2;i++){
	    
	     d=p.size()-1;
      int temp=p[d]-i;
      p.push_back(temp);
      p[d]=p[d]-temp;
      d=p.size()-1;
      // cout<<"i= "<<i<<endl;
      sort(p.data(),p.data()+d+1);
      // cout<<ctr<<" d= "<<d<<" i= "<<i<<endl;
      r=min(min(solve(p,d,ctr),solve(q,d-1,ctr)),r);
      // ctr++;
      p=o;
      /*  cout<<"p"<<endl;
       for(int j=0;j<p.size();j++){
	     cout<<p[j]<<"\t";
	 }
       cout<<endl;*/
       }
        return r;
}
int main()
{
      int T,d;
      vector<int> p;
      int ctr=0,an;
      cin>>T;
      for(int i=0;i<T;i++){
	    cin>>d;
	    for(int j=0;j<d;j++) {
		  cin>>an;
		  p.push_back(an);
		  // q.push_back(an);
	    }
	    sort(p.data(),p.data()+d);
	    an=solve(p,d-1,ctr);
	    printf("Case #%d: %d\n",i+1,an);
	    for(int j=0;j<d;j++) {
		  p.clear();
		  // q.clear();
	    }
      }
}
