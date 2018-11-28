#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
  int testcases;
  cin>>testcases;
  for(int t=0;t<testcases;t++)
  {
    int n;
    cin>>n;
    //double nami[10] = {0.186,0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899};
    //double ken[10] = {0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458};
    double nami[n],ken[n];
    double namidesc[n],kendesc[n];
    for(int p=0;p<n;p++)
	 cin>>nami[p];
    for(int p=0;p<n;p++)
	 cin>>ken[p];
    sort(nami,nami+n);
    sort(ken,ken+n);
    int deceitfulCount =0;
    int normalCount =0;
    for(int i=0;i<n;i++)
    {
	 namidesc[n-i-1] = nami[i];
	 kendesc[n-i-1] = ken[i];
    }
    
 
  int i=0,j=0;
  while(j<n&&i<n)
  {
    if(nami[j]<ken[i])
    {
	 normalCount++;
	 i++;
	 j++;
    }
    else
    {
	 i++;
    }
  }
  
  i=0,j=0;
  while(i<n&&j<n)
  {
    if(namidesc[j]>kendesc[i])
	 {
	   deceitfulCount++;
	   i++;
	   j++;
	 }
	 else
	 {
	   i++;
	 }
  }
 /*for(int i=0;i<9;i++)
 {
    cout<<nami[i]<<" "<<ken[i]<<"\n";
 }
 
 cout<<"------------------------------------"<<"\n";
 for(int i=0;i<9;i++)
 {
    cout<<nami[i]<<" "<<ken[8-i]<<"\n";
 }*/
 
 cout<<"Case #"<<t+1<<": "<<deceitfulCount<<" "<<n-normalCount<<"\n";	
  }
}