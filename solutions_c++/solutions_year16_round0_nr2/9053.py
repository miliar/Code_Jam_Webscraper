#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int input[1000000];
    ofstream op_file;
    op_file.open("output_file");
    char a;
    //string s;
    int input_count=0, rem;
    //read the input file
    ifstream file_h;
    string sl;
    file_h.open("B-large.in");
    file_h>>input[0];
    std::getline(file_h,sl);
    cout<<input[0];
    for(int i=1; i<=input[0]; i++)
    {
    string s;
    int k=0,stp=0,cond=0;
     std::getline(file_h,s);

     while(s[k]!='\0'){

        while(s[k]=='-')k++;

cout<<endl<<s[k-1]<<' '<<s[k]<<endl;
        if(s[k-1]=='-' && s[k]=='+');
        //stp++;
        while(s[k]=='+')k++;
        if(s[k-1]=='+' && s[k]=='-')
        {stp=stp+2;}

     }
     if(s[0]=='-')stp++;
    // if(cond==1)stp++;

     op_file<<"Case #"<<i<<": "<<stp<<endl;
    // if(a=='+')
     //s[i]=1;

    }
    file_h.close();


    op_file.close();
    return 0;
    //for(int i=0; i<;i++){
    //cout << input[i]<< endl;
    //}
}
