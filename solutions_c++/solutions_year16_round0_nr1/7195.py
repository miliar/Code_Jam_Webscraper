#include<iostream>
#include<string>
#include<fstream>

using namespace std;

long long int nod(long long int n){ long long int l=0;
                  while(n){
                  l++;
                  n=n/10;
                  }
                  return l;}

int main(){   ifstream in("input.in");
               ofstream out("output.in");
               long long int t,a;
               in>>t;
               for(a=1;a<t+1;a++)
               {

                     long long int no,n;
                in>>no;
                if(no==0)
                { out<<"Case #"<<a<<": INSOMNIA"<<endl;
                   continue;
                }
               n=no;
             long long int arr[10];
            for(long long int i=0;i<10;i++)
            arr[i]=999;

            long long int p=1;
            while(1)
                {
                      long long int k=nod(n);
                      long long int num=n;
              for(long long int i=1;i<k+1;i++){

                  long long int d=num%10;
                  arr[d]=d;
                       num=num/10;
              }
              long long int c=0;
            for(long long int i=0;i<10;i++)
            {if(arr[i]==i)
               c++;
             }
            if(c==10)
                break;
             else { p++;
                    n=p*no;
                   }
            }
        out<<"Case #"<<a<<": "<<p*no<<endl;

               }

         return 0;
          }
