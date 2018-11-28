#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    std::ifstream infile("input1.txt");
    std::ofstream output("output1.txt");
    int T;
     infile>>T;

     //cin>>T;
     int x;
 for(x=1;x<=T;++x)
 {
                  int ans = 0;
          int A,N,i,j;
         infile>>A>>N;
         // cin>>A>>N;

          int arr[N];

          for(i=0;i<N;++i)
          {
                      infile>>arr[i];
              //         cin>>arr[i];
          }
          int c,d;
          for (c = 0 ; c < N ; c++) {
              d = c;

                while ( d > 0 && arr[d] < arr[d-1]) {
                int t          = arr[d];
                arr[d]   = arr[d-1];
                arr[d-1] = t;

                d--;
                }
                }

       int prevSum = A;
       int flag = 0;
                for(i=0;i<N;i++){

                             
                                if(i==N-1)
                                {
                                    if(prevSum<=arr[i])
                                    ans = ans+1;

                                }
                                
                                
                                 else
                                 {int j=0;
                                 while(prevSum<=arr[i]){
                                                        j = j+1;
                                                        ans = ans +1;
                                              prevSum = (2*prevSum) - 1;

                                              //i = i+1;
                                                        if(j== (N-i)){
                                                               flag =1;
                                                               break;
                                                        }


                                 }
                                 if(flag == 1){
                                         break;
                                 }
                                 else {
                                      if(prevSum>arr[i]  ){
                                                        prevSum = prevSum+arr[i];
                                      }
                                 }

                                 }
                }








           output<<"Case #"<<x<<": "<<ans<<endl;
           //cout<<ans<< endl;

 }//while T--




    //system("pause");
    return 0;
}
