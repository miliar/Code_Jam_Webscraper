#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;
int main(){
    ifstream fin("C-small-attempt0.in");
    ofstream fout("output.out");
    
    int cases;
    fin>>cases;
    //char tictac[4][4];
    
    for(int i=0; i<cases; i++)
    {
        int base, limit;
        fin>>base>>limit;
        //cout<<base<<"  "<<limit<<endl;
        int test = int (sqrt(base));
        int result = test * test;
        int count =0;
       // cout<<result<<">"<<base<<"  "<<result<<"<"<<limit;
        while(result<base){ test = test +1; result = test * test;}
        while(result >= base && result <= limit)
        {
            int n = result;
            int testn = test;
            int rev = 0;
            int dig = 0;
            while (result > 0)
            {
              dig = result % 10;
              rev = rev * 10 + dig;
              result = result / 10;
            }
            
            int trev = 0;
            while (testn > 0)
            {
              dig = testn % 10;
              trev = trev * 10 + dig;
              testn = testn / 10;
            }
            
            //cout<<"n = "<<n<<" rev = "<< rev<<endl;
            if(n == rev && test == trev){
                //cout<<"n = "<<n<<" test = "<<test<<"   ";
                count++;
            }
            test +=1;
            result = test * test;
        }
        //cout<<endl;
        fout<<"Case #"<<i+1<<": "<<count<<endl;
        //cout<<"Case #"<<i+1<<": Draw"<<endl;
    }
    
    fin.close();
    fout.close();
    //system("pause");
    return 0;   
}
