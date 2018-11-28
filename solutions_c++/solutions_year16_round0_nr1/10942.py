#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int T=0;
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("Counting Output1.txt");
    in >>T;
    for(int s=0;s<T;s++)
    {
    long int num=0;
    int flag=0;
    int arrFlag=0;

    in >>num;
    out <<"Case #"<<s+1<<": ";
    int arr[10]={-5,-5,-5,-5,-5,-5,-5,-5,-5,-5};
    char check;
    if(num==0){
        out <<"INSOMNIA"<<endl;
    }
    else{
            int f=1;
            int num1=num;
        while(flag!=10)
        {
            int numBackup=num1;
           while (numBackup>0)
           {
               int modulo=numBackup%10;
               int i=0;
               for(i=0;i<10&&arr[i]!=-5;i++){
                    if(arr[i]==modulo)
                    {
                        arrFlag=1;
                    }
               }
               if(arrFlag==0){
                    arr[i]=modulo;
                    flag++;
           // cout <<endl<<"Value of num is="<<num1<<" Flags are="<<flag<<endl<<endl;
           for(int j=0;j<10;j++)
           {
           //    cout << arr[j]<<" ";
           }
               }
               arrFlag=0;
               numBackup/=10;
           //    cout << "Inner LOOP";
           }
            f++;
           if(flag==10)
           {
               out << num1<<endl;
           }
           if(f==100000)
           {
               out <<"INSOMNIA"<<endl;
               break;
           }
           num1=num*f;
          // cin >>check;
        }

    }


    }

}
