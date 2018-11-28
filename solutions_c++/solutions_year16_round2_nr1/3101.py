#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

unsigned short int str2usi(string temp){
    unsigned short int out;
    stringstream strStream;
    strStream << temp;
    strStream >> out;
    return out;
}


string strSearch(string &str){
    string strOut;
    int nDig, tmp1=0, tmp2=0;

    int N[10];
    for(int i=0; i<10; ++i)
        N[i]=0;

    // Search Zeros
    while((tmp1 = str.find('Z', tmp1)) >= 0 ){
        str[tmp1] = '0';

        str[str.find('E')] = '0';
        str[str.find('R')] = '0';
        str[str.find('O')] = '0';
        ++N[0];
    }
    cout<<"0: "<<N[0]<<"  |";

    // Search Six
    tmp1 = 0;
    while((tmp1 = str.find('X', tmp1)) >= 0 ){
        str[tmp1] = '6';

        str[str.find('I')] = '6';
        str[str.find('S')] = '6';
        ++N[6];
    }
    cout<<"6: "<<N[6]<<"  |";

    // Search Four
    tmp1 = 0;
    while((tmp1 = str.find('U', tmp1)) >= 0 ){
        str[tmp1] = '4';

        str[str.find('F')] = '4';
        str[str.find('O')] = '4';
        str[str.find('R')] = '4';
        ++N[4];
    }
    cout<<"4: "<<N[4]<<"  |";

    // Search Eight
    tmp1 = 0;
    while((tmp1 = str.find('G', tmp1)) >= 0 ){
        str[tmp1] = '8';

        str[str.find('E')] = '8';
        str[str.find('I')] = '8';
        str[str.find('H')] = '8';
        str[str.find('T')] = '8';
        ++N[8];
    }
    cout<<"8: "<<N[8]<<"  |";

    // Search Two
    tmp1 = 0;
    while((tmp1 = str.find('W', tmp1)) >= 0 ){
        str[tmp1] = '2';

        str[str.find('T')] = '2';
        str[str.find('O')] = '2';
        ++N[2];
    }
    cout<<"2: "<<N[2]<<"  |";

    // Search One
    tmp1 = 0;
    while((tmp1 = str.find('O', tmp1)) >= 0 ){
        str[tmp1] = '1';

        str[str.find('N')] = '1';
        str[str.find('E')] = '1';
        ++N[1];
    }
    cout<<"1: "<<N[1]<<"  |";

    // Search Three
    tmp1 = 0;
    while((tmp1 = str.find('R', tmp1)) >= 0 ){
        str[tmp1] = '3';

        str[str.find('T')] = '3';
        str[str.find('H')] = '3';
        str[str.find('E')] = '3';
        str[str.find('E')] = '3';
        ++N[3];
    }
    cout<<"3: "<<N[3]<<"  |";

    // Search Five
    tmp1 = 0;
    while((tmp1 = str.find('F', tmp1)) >= 0 ){
        str[tmp1] = '5';

        str[str.find('I')] = '5';
        str[str.find('V')] = '5';
        str[str.find('E')] = '5';
        ++N[5];
    }
    cout<<"5: "<<N[5]<<"  |";

    // Search Seven
    tmp1 = 0;
    while((tmp1 = str.find('S', tmp1)) >= 0 ){
        str[tmp1] = '7';

        str[str.find('E')] = '7';
        str[str.find('V')] = '7';
        str[str.find('E')] = '7';
        str[str.find('N')] = '7';
        ++N[7];
    }
    cout<<"7: "<<N[7]<<"  |";

    // Search Nine
    tmp1 = 0;
    while((tmp1 = str.find('I', tmp1)) >= 0 ){
        str[tmp1] = '9';

        str[str.find('N')] = '9';
        str[str.find('N')] = '9';
        str[str.find('E')] = '9';
        ++N[9];
    }
    cout<<"9: "<<N[9]<<"  |"<<endl;


    for(int i=0; i<N[0];++i)
        strOut.push_back('0');

    for(int i=0; i<N[1];++i)
        strOut.push_back('1');

    for(int i=0; i<N[2];++i)
        strOut.push_back('2');

    for(int i=0; i<N[3];++i)
        strOut.push_back('3');

    for(int i=0; i<N[4];++i)
        strOut.push_back('4');

    for(int i=0; i<N[5];++i)
        strOut.push_back('5');

    for(int i=0; i<N[6];++i)
        strOut.push_back('6');

    for(int i=0; i<N[7];++i)
        strOut.push_back('7');

    for(int i=0; i<N[8];++i)
        strOut.push_back('8');

    for(int i=0; i<N[9];++i)
        strOut.push_back('9');

    return strOut;
}


int main(){

    ifstream inFile;
    ofstream outFile;

    unsigned short int num_Cases;
    // <--->

    string S;

    // <--->
    inFile.open("A-large.in.txt");
    outFile.open("Large_Result.txt");

    getline(inFile,S);
    num_Cases = str2usi(S);

    cout<<"N Cases: "<<num_Cases<<endl;

    for(int i = 0; i < num_Cases; ++i){

        // Get String
        getline(inFile,S);

        cout<<"String: "<< S <<endl;
        // <--->

        // <--->
        outFile<<"Case #"<<i+1<<": "<< strSearch(S) << endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
