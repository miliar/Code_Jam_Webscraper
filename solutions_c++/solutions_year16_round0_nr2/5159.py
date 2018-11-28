#include <bits/stdc++.h>

using namespace std;

#define ll long long
//#define cout cerr
string error;
    
ll solver()
{
  ll endofplus=-1;
  string temp=error;
  ll google=0;
  while(1)
  {

    ll ans=0;
   for(ll i=0;i<temp.length();i++)
    if(temp[i]=='+')
      ans++;
    if(ans==temp.length())
      break;
    
    //cout<<"entering step "<<google<<endl;
  for(ll i=0;i<temp.length();i++)
  {
    if(temp[i]=='-')
      break;
    endofplus=i;
  }
  //cout<<"endofplus is "<<endofplus<<endl;
  if(endofplus!=-1)
    {
      for(ll j=0;j<=endofplus;j++)
        temp[j]='-';
      google++;
     // reverse(temp.begin(),temp.begin()+endofplus+1);
    //cout<<"converted to "<<temp<<endl;
    }
    
    ll lastminus=-1;
    for(ll i=0;i<temp.length();i++)
      if(temp[i]=='-')
        lastminus=i;
      //cout<<"lastminus is "<<lastminus<<endl;
    if(lastminus!=-1)
    {
      //cout<<"before swapping "<<temp<<endl;
      for(ll i=0;i<=lastminus;i++)
      {
        if(temp[i]=='-')
          temp[i]='+';
        else temp[i]='-';
      }
      //cout<<"after inverting "<<temp<<endl;
      google++;
      reverse(temp.begin(),temp.begin()+lastminus+1);
      //cout<<"converted to "<<temp<<endl;
    }
    
    //cout<<"after this step temp is "<<temp<<endl;
 }

return google;
}

int main()
{
  ll t;
  cin>>t;
  for(ll cases=1;cases<=t;cases++)
  {
   // cout<<endl<<endl;
    

    cin>>error;
    printf("Case #%lld: ",cases );
    printf("%lld\n",solver());
//    cout<<solver()<<endl;


    
  } 
  return 0; 
}