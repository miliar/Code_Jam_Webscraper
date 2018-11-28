#include <set>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

int main()
{

    char t[10];
    ifstream f;
    f.open("c:\\input.txt");
    f.getline(t,10);

    ofstream o;
    o.open("c:\\output.txt");
    char out[100];
    int i = atoi(t);
    
    for(int k=1; k<=i;k++)
    {
        int flag =0;
        char num[50]; 
        f.getline(num, 50);
        int n=atoi(num);
        //int sz = strlen(num);
        set<char> s;
        //for(int i=0;i<sz;i++)
          //  s.insert(num[i]);
        
        char buff[50];
        memset(buff, '0', 50);
        int mult=1;
        int prev=0;
        while(s.size() < 10)
        {      
           int pr=n*mult;
           if(pr == prev){
               sprintf(out, "Case #%d: INSOMNIA\n", k);
               o << out;
               flag=1;
               break;
           }          
                      
           itoa(pr, buff, 10);
           int sz1 = strlen(buff);
           for(int i=0;i<sz1;i++)
            s.insert(buff[i]);
           prev = pr;
           mult += 1;
        }
        
        if(!flag){         
          sprintf(out, "Case #%d: %d\n", k, prev);
          o << out;
        }
    }

    f.close();
    o.close();
    return 0;
}
