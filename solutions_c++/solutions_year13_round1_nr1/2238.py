#include<iostream>
#include<conio.h>
#include<stdio.h>
using namespace std;
int main()
{
    int out_edge, in_edge,r,t=1,testcase,rem_paint,rings=1;
    freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	cin>>testcase;
	while(t<=testcase)
	{
       rings=1;
      cin>>r>>rem_paint;
      in_edge=r;
      out_edge=r+1;
      rem_paint=rem_paint-(out_edge*out_edge-in_edge*in_edge);        
      while(rem_paint>0)    
      {
             //cout<<out_edge<<" "<<in_edge<<" ";
             out_edge+=2;
             in_edge+=2;
             rem_paint=rem_paint-(out_edge*out_edge-in_edge*in_edge);
             //cout<<rem_paint<<" ";
             if (rem_paint>=0) rings++;
             //cout<<rings<<endl;              
      } 
      cout<<"Case #"<<t<<": "<<rings<<endl;     
      t++;  
    }
    return 0;
}
