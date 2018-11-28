/* Code Jam 2014
@Author: Jugesh Sundram
*/

#include <iostream>
#include <conio.h>
#include <iomanip> // for setprecision()

using namespace std;

int main(){

freopen("B-large.in", "r", stdin);
freopen("B-large.out", "w", stdout);
 
//freopen("test_data.txt", "r", stdin);
//freopen("test_result.out", "w", stdout);
   cout << setprecision(12);
  int test_count;
  cin >> test_count;
  
  for (int test_index = 0; test_index < test_count; ++test_index) {
  
  double C,F,X,last_sum = 0.0;

  cin>>C>>F>>X;

  if(X/2 < C/2 + X/(F+2))
  {//printf("C:%.7f F:%.5f X:%.5f\n",C,F,X);
  printf("Case #%d: %.9f\n",test_index+1,X/2);
}

  else
  {
  for(int idx=0;idx<200000;idx++)
  {
   double sum = 0.0000000;
   for(int i = 0 ; i<=idx ; i++)
   {
    //printf("%.7f + ",C/(i*F+2));       
   // cout<<C/(i*F+2)<<" + ";       
    sum += C/(i*F+2);
     
   }
   sum +=  X/((idx+1)*F+2);
 //  cout<<X/((idx+1)*F+2);cout<<" = "<<sum<<endl;
   
      
   if(idx == 0)
   last_sum = sum;
   
     
   if(sum > last_sum)
    {//cout<<"idx: "<<idx<<" ";
     break;}
    
   else
       last_sum = sum;
       
    
  }
  //printf("C:%.7f F:%.5f X:%.5f\n",C,F,X);
  //cout<<"Case #"<<test_index+1<<": "<<last_sum<<"\n";
  printf("Case #%d: %.9f\n",test_index+1,last_sum);
  }


  }
	
	return 0;
}

// cout << "Case #" << test_index + 1 << ": "<<result<<endl;
