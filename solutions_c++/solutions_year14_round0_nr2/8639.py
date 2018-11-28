#include<iostream>
#include<iomanip>

using namespace std;

void solveCookie(int );

int main()
{
 int N=0,i=0;
 cin>>N;   //number of test cases
 cout<<"\n";
 
 for(i=0; i<N;i++)
 {
   solveCookie(i+1);   
 } 
 return 0;
}

void solveCookie(int Case)
{
  double start=2.0;
  double C, F=0, X, Seconds=0.0;
  //get first number
  cin>>C>>F>>X;
  double dOldCTime,dNewXTime=0.0, dOldXTime=0.0, dNewCTime, oldSeconds=0.0;

  dOldCTime = C/start;
  dOldXTime = X/start;  
  Seconds+= dOldCTime;
  oldSeconds = dOldCTime;

  while(1)
  {
     start += F;
     dNewXTime = X/start;
     dNewCTime = C/start;

     if(dOldCTime + dNewXTime > dOldXTime)
     {
       Seconds-=oldSeconds;
       break;
     }
     Seconds += dNewCTime;
     oldSeconds = dNewCTime;
     dOldCTime = dNewCTime;
     dOldXTime = dNewXTime;
  }
  cout.precision(7);
  cout.setf( std::ios::fixed, std:: ios::floatfield);
  cout<<"Case #"<<Case<<": "<<Seconds+dOldXTime<<"\n";
  
}

