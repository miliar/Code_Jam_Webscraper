#include<iostream>
using namespace std;

int main()
{   int test,chart,i;
    std::cin>>test;
    char result[1010],cons,tempc;
    std::string n,temp;
    cin.ignore();
    for(int cs=1;cs<=test;cs++){
        std::cin>>n;
        i=1;
        result[0]=n[0];

      //  std::cout<<result<<"\t is"<<result[0];
        while(i<=n.length()){
            if(n[i]<result[0]){
                result[i]=n[i];
            }
            else{
          //      std::cout<<result[0]<<" is l "<<n[i];
                cons=result[0];
                for(int j=0;j<i;j++){
                    tempc=cons;
                    cons=result[j+1];

                    result[j+1]=tempc;
                }
                //std::cout<<"result is "<<result;
                result[0]=n[i];
            }
            i++;
          //  std::cout<<"Case #"<<cs<<": "<<result<<"\t"<<temp<<"\t"<<n<<endl;


        }


        std::cout<<"Case #"<<cs<<": "<<result<<endl;
      /*   i=0;
            while(i<=n.length()){
                std::cout<<result[i];
                i++;
            }*/
    }
    return 0;
}

