#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<typeinfo>

using namespace std;
int palindrome(float a) {
    int temp = a;
    int sum=0,r;
    while(temp){
        r=temp%10;
        temp=temp/10;
        sum=sum*10+r;
    }
    if(a==sum)
        return 1;
    else
        return 0;
}
int main()
{
    int test_cases;
    string x;

    ifstream inFile;
    ofstream outFile;
    outFile.open("out.txt");
    inFile.open("data.in");
    
    inFile>>x;
    test_cases = atoi(x.c_str());
    for(int i=0;i<test_cases;i++) {
        inFile>>x;
        int A = atoi(x.c_str());
        inFile>>x;
        int B = atoi(x.c_str());
        int count=0;
        for(int j=A;j<=B;j++) {
            int result=palindrome(j)&&palindrome(sqrt(j));
            if(result) {
                count++;
            }
            }
        outFile << "Case #"<<i+1<<": "<<count<<endl;
    }
    return 0;
}

