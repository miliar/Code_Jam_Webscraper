#include<iostream>
#include<fstream>

using namespace std;

int c[10] = {0};

int main(){
    int N = 1, i=1, fin = 0, Case, Number, iNumber, n, digit=0,j=0;
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("Output.txt");
    in >> Case;
    N = Case;
    while(Case>0){
        in >> Number;
        if(Number == 0){
            cout << "Case #" << N-Case+1 << ": INSOMNIA" << endl;
            out << "Case #" << N-Case+1 << ": INSOMNIA" << endl;
            Case-=1;
            continue;
        }
        while(fin!=10){
            iNumber = i * Number;

            do{
                digit = iNumber%10;
                switch(digit){
                    case 0: c[0] = 1; break;
                    case 1: c[1] = 1; break;
                    case 2: c[2] = 1; break;
                    case 3: c[3] = 1; break;
                    case 4: c[4] = 1; break;
                    case 5: c[5] = 1; break;
                    case 6: c[6] = 1; break;
                    case 7: c[7] = 1; break;
                    case 8: c[8] = 1; break;
                    case 9: c[9] = 1; break;
                }
                iNumber /= 10;
            }while(iNumber >0);

            i+=1;
            fin = c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+c[8]+c[9];
        }
        cout << "Case #" << N-Case+1 << ": " << Number * (i-1) << endl;
        out << "Case #" << N-Case+1 << ": " << Number * (i-1) << endl;
        i = 1;
        fin = 0;
        Case-=1;
        for(j=0;j<10;j++) c[j] = 0;
    }
    in.close();
    out.close();
    return 0;
}


