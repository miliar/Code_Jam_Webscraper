#include <iostream>
#include <fstream>
using namespace std;



int main (){
    ifstream in("Al.in");
    ofstream out("aloutput.txt");

    int testcases;
    in >> testcases;
    char k=in.get();
    int testcasses = testcases;
    while (testcasses -->0){
        int znwhuvxsgi[10];
        int cijfers[10];
        for (int i=0;i<10;i++){
            znwhuvxsgi[i]=0;
            cijfers[i]=0;
        }
        char k=in.get();
        while(k!='\n'){
            switch(k){
                case 'Z':
                    znwhuvxsgi[0]++;
                    break;
                case 'N':
                    znwhuvxsgi[1]++;
                    break;
                case 'W':
                    znwhuvxsgi[2]++;
                    break;
                case 'H':
                    znwhuvxsgi[3]++;
                    break;
                case 'U':
                    znwhuvxsgi[4]++;
                    break;
                case 'V':
                    znwhuvxsgi[5]++;
                    break;
                case 'X':
                    znwhuvxsgi[6]++;
                    break;
                case 'S':
                    znwhuvxsgi[7]++;
                    break;
                case 'G':
                    znwhuvxsgi[8]++;
                    break;
                case 'I':
                    znwhuvxsgi[9]++;
                    break;
            }
            k=in.get();
        }
        while(znwhuvxsgi[0]!=0){
            znwhuvxsgi[0]--;
            cijfers[0]++;
        }
        while(znwhuvxsgi[6]!=0){
            znwhuvxsgi[6]--;
            znwhuvxsgi[7]--;
            znwhuvxsgi[9]--;
            cijfers[6]++;
        }
        while(znwhuvxsgi[7]!=0){
            znwhuvxsgi[7]--;
            znwhuvxsgi[1]--;
            znwhuvxsgi[5]--;
            cijfers[7]++;
        }
        while(znwhuvxsgi[5]!=0){
            znwhuvxsgi[5]--;
            znwhuvxsgi[9]--;
            cijfers[5]++;
        }
        while(znwhuvxsgi[8]!=0){
            znwhuvxsgi[8]--;
            znwhuvxsgi[3]--;
            znwhuvxsgi[9]--;
            cijfers[8]++;
        }
        while(znwhuvxsgi[9]!=0){
            znwhuvxsgi[9]--;
            znwhuvxsgi[1]--;
            znwhuvxsgi[1]--;
            cijfers[9]++;
        }
        while(znwhuvxsgi[4]!=0){
            znwhuvxsgi[4]--;
            cijfers[4]++;
        }
        while(znwhuvxsgi[3]!=0){
            znwhuvxsgi[3]--;
            cijfers[3]++;
        }
        while(znwhuvxsgi[2]!=0){
            znwhuvxsgi[2]--;
            cijfers[2]++;
        }
        while(znwhuvxsgi[1]!=0){
            znwhuvxsgi[1]--;
            cijfers[1]++;
        }
        out<<"Case #"<<testcases-testcasses<<": ";
        for(int i=0;i<10;i++){
            while(cijfers[i]!=0){
                out<<i;
        cijfers[i]--;
            }
        }
        out<<endl;
    }
    return 0;
}
