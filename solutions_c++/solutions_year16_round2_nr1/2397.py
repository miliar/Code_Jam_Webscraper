#include <iostream>
#include<string>
#include<map>
#include<fstream>
using namespace std;
int num[11];
map<char,int>m;
int charnum[40];
int ci(char c){
    return (int)(c-'A');
}
int main()
{
    ifstream in;
    ofstream out;
    in.open("E:\\project\\A-large(2).in");
    out.open("E:\\project\\round1(2)-a-large.txt");
    int t,k=0;
    string s;

    in>>t;
    while(t--){
        m.clear();
        k++;
        in>>s;
        for(int i=0;i<40;i++)charnum[i]=0;
        for(int i=0;i<s.length();i++){
            charnum[(int)(s[i]-'A')]++;
        }
        for(int i=0;i<11;i++)num[i]=0;
        while(charnum[ci('Z')]>0){//0
            charnum[ci('Z')]--;
            charnum[ci('E')]--;
            charnum[ci('R')]--;
            charnum[ci('O')]--;
            num[0]++;
        }
        while(charnum[ci('W')]>0){//2
            charnum[ci('T')]--;
            charnum[ci('W')]--;
            charnum[ci('O')]--;
            num[2]++;
        }
        while(charnum[ci('X')]>0){//6
            charnum[ci('S')]--;
            charnum[ci('I')]--;
            charnum[ci('X')]--;
            num[6]++;
        }
        while(charnum[ci('G')]>0){//8
            charnum[ci('E')]--;
            charnum[ci('I')]--;
            charnum[ci('G')]--;
            charnum[ci('H')]--;
            charnum[ci('T')]--;
            num[8]++;
        }
        while(charnum[ci('T')]>0){//3
            charnum[ci('T')]--;
            charnum[ci('H')]--;
            charnum[ci('R')]--;
            charnum[ci('E')]--;
            charnum[ci('E')]--;
            num[3]++;
        }
        while(charnum[ci('R')]>0){//4
            charnum[ci('F')]--;
            charnum[ci('O')]--;
            charnum[ci('U')]--;
            charnum[ci('R')]--;
            num[4]++;
        }
        while(charnum[ci('O')]>0){//1
            charnum[ci('O')]--;
            charnum[ci('N')]--;
            charnum[ci('E')]--;
            num[1]++;
        }
        while(charnum[ci('F')]>0){//5
            charnum[ci('F')]--;
            charnum[ci('I')]--;
            charnum[ci('V')]--;
            charnum[ci('E')]--;
            num[5]++;
        }
        while(charnum[ci('S')]>0){//7
            charnum[ci('S')]--;
            charnum[ci('E')]--;
            charnum[ci('V')]--;
            charnum[ci('E')]--;
            charnum[ci('N')]--;
            num[7]++;
        }
        while(charnum[ci('N')]>0){//9
            charnum[ci('N')]--;
            charnum[ci('I')]--;
            charnum[ci('N')]--;
            charnum[ci('E')]--;
            num[9]++;
        }
        out<<"Case #"<<k<<": ";
        for(int i=0;i<10;i++){
            for(int j=0;j<num[i];j++)out<<i;
        }
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
