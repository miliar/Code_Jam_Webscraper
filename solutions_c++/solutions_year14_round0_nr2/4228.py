#include<iostream>
#include<fstream>

using namespace std;

int main() {

 ifstream myReadFile;
 ofstream outfile;
 myReadFile.open("B-large.in");
 outfile.open("out.out");
 int casos;
long double total, costefab, produc, value, velocidad=2;
 if (myReadFile.is_open()) {
    
    myReadFile >> casos;
    //cout << casos;
    for(int i=0; i < casos; i++){
        myReadFile >> costefab >> produc >> total;
        value=0;
        velocidad=2;
        //cout<< value << endl;
        while(true){
            if((costefab/velocidad)+total/(velocidad+produc)<total/velocidad){
                value+=costefab/velocidad;
                //cout << value << endl;
                velocidad=velocidad+produc;
            }
            else break; 
        }
        value+=total/velocidad;
        cout.precision(10);
        cout << value <<endl;
        outfile.precision(10);
        outfile << "Case #" << i+1 << ": " << (double)value;
        if(i!=casos-1)outfile << endl;
    }   
}
myReadFile.close();
system("pause");
return 0;
}
