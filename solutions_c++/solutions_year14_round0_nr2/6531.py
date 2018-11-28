#include <algorithm>
#include <bitset>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

int main()
{
	freopen("in.txt", "r",stdin);
    freopen("out.txt", "w",stdout);
  	//double a=83.3333333;
	//printf("%.7f\n", a);    
    int n;
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
    	double c,f,x;
    	cin>>c>>f>>x;
    	 double partialTime=0;
    	  double finalTime=0;
    	 bool v=false;
    	 double sum=2.0; 
    	 while(!v)
    	 {
    	 	//cout<<" x : ";
    	 	//printf("%.7f\n", x);
    	 	//cout<<" sum : ";
    	 	//printf("%.7f\n", sum);
    	 	double ev1=x/sum;
    	 	//cout<<"ev1 : ";
    	 	//printf("%.7f\n", ev1);
    	 	   	 	//50
    	 	double ev2=(c/sum)+x/(sum+f);
    	 		//15+25
    	 	//cout<<"ev2 : ";
    	 	//printf("%.7f\n", ev2);
    	 	if(ev1<=ev2)
    	 	{
    	 		v=true;
    	 		finalTime=partialTime+ev1;
    	 	}else
    	 	{
    	 		partialTime+=c/sum;
    	 		//cout<<"partialTime : ";    	 	
    	 		//printf("%.7f\n", partialTime);	
    	 	
    	 	}

    	 	sum+=f;
    	 }
    	 cout<<"Case #"<<i+1<<": ";
    	 printf("%.7f\n", finalTime);
    	 //cout<<"-------------------------------------------------------------"<<endl;

    }
    

 }