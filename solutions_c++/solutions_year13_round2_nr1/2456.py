#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    std::ifstream infile("input1.txt");
    std::ofstream output("output1.txt");
    int T;
     infile>>T;
    int x;
 for(x=1;x<=T;++x)
 {
                  int answer = 0;
          int A,N,i,j;
          infile>>A>>N;
        int in[N];

          for(i=0;i<N;++i)
          {
                       infile>>in[i];

          }
          int c,d;
          for (c = 0 ; c < N ; c++) {
              d = c;

                while ( d > 0 && in[d] < in[d-1]) {
                int t          = in[d];
                in[d]   = in[d-1];
                in[d-1] = t;

                d--;
                }
                }

       int presum = A;
       int temp = 0;
                for(i=0;i<N;i++){

                                if(i==N-1)
                                {
                                    if(presum<=in[i])
                                    answer = answer+1;

                                }

                                 else
                                 {
                                     int j=0;
                                 while(presum<=in[i])
                                    {
                                                        j = j+1;
                                                        answer = answer +1;
                                              presum = (2*presum) - 1;

                                              //i = i+1;
                                                        if(j== (N-i)){
                                                               temp =1;
                                                               break;
                                                        }


                                 }
                                 if(temp == 1){
                                         break;
                                 }
                                 else {
                                      if(presum>in[i]  ){
                                                        presum = presum+in[i];
                                      }
                                 }

                                 }
                }








           output<<"Case #"<<x<<": "<<answer<<endl;


 }//while T--




    //system("pause");
    return 0;
}
