#include<fstream>
using namespace std;
int main(){
    int T;
    int *Smax;
    int i,j,out;
    int sum;
    ifstream ifs;
    ofstream ofs;
    ofs.open("1smalloutput.txt");
    ifs.open("1small.txt");
    ifs>>T;
    char *arr[T];
    Smax= new int[T];
    for(i=0;i<T;i++)
    {

        ifs>>Smax[i];
        arr[i]=new char[Smax[i]+1];
        ifs>>arr[i];
    }
    for(i=0;i<T;i++){
        out=0;
        sum=arr[i][0]-'0';
        for(j=1;j<=Smax[i];j++)
        {
            if(arr[i][j]-'0'!=0)
            {
                    if(sum<j )
                    {

                        out=out+(j-sum);
                        sum=out+sum+(arr[i][j]-'0');
                    }
                    else
                        sum=sum+(arr[i][j]-'0');
            }

        }
        ofs<<"Case #"<<(i+1)<<": "<<out<<"\n";
    }

    return 0;
}
