#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
     int n;
     cin>>n;
	 for(int i=0;i<n;i++)
     {
          bool table[16] =  {0};
          int a,b,a1,a2,a3,a4,b1,b2,b3,b4;
          cin>>a;
          for(int j=0; j<4; j++)
          {
        	cin >> a1;
          	cin >> a2;          
          	cin >> a3;
          	cin >> a4;
          	if(j==(a-1))
			  {
          		table[a1-1] = true;
  	        	table[a2-1] = true;
		        table[a3-1] = true;
		        table[a4-1] = true;
          	}
          }
          
          cin >> b;          
          for(int j=0; j<4; j++)
          {
          	cin >> b1;
          	cin >> b2;          
          	cin >> b3;
          	cin >> b4;
          	
          	if(j==(b-1)){
          			int commoncount = 0;
          int commonelement;
          if(table[b1-1]) {commoncount++; commonelement = b1;}
          if(table[b2-1]) {commoncount++; commonelement = b2;}
          if(table[b3-1]) {commoncount++; commonelement = b3;}
          if(table[b4-1]) {commoncount++; commonelement = b4;}
          
          cout<<"Case #"<<i+1<<": ";
          if(commoncount == 0) cout<<"Volunteer cheated!";
          if(commoncount > 1) cout<<"Bad magician!";
          if(commoncount == 1) cout<<commonelement;
          cout<<endl;
          	}
    }
      }
	 return 0;     
}
