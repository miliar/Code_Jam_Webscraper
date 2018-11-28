#include <bits/stdc++.h>
using namespace std;

long long toInt(string s) {
    long long tmp = 0;
    for(int c=0;c<s.size();c++) {
        tmp = tmp*10+s[c]-'0';
    }
    return tmp;
}


long long best = 1e19;
long long res1Val,res2Val;
string res1,res2;

void actualise(string s,string s2) {

    long long one = toInt(s);
    long long two = toInt(s2);
    long long diff = abs(one-two);

    if(diff < best) {
        best = diff;
        res1 = s;
        res2 = s2;
        res1Val = one;
        res2Val = two;
    }
    else if(diff == best && (res1Val > one || (res1Val == one && res2Val > two))) {
        best = diff;
        res1 = s;
        res2 = s2;
        res1Val = one;
        res2Val = two;
    }
}

void generateInf(string s,string s2,int i, bool swapounet) {
    if(i==s.size()) {
        if(swapounet) actualise(s2,s);
        else actualise(s,s2);
        return;
    }
    char ori1 = s[i],ori2=s2[i];
    if(s[i]=='?') {
        s[i]='9';
    }
    if(s2[i]=='?') {
        s2[i]='0';
    }
    generateInf(s,s2,i+1,swapounet);
    s[i]=ori1;
    s2[i]=ori2;
}

void generateOne(string s, string s2, int i) {

    if(i==s.size()){
        actualise(s,s2);
        return;
    }

    if(s[i]=='?' && s2[i]=='?'){
        s[i] = '0';
        s2[i] = '0';
        generateOne(s,s2,i+1);
        s[i] = '9';
        generateInf(s,s2,i+1,false);
        s[i]='0';
        s2[i]='9';
        generateInf(s2,s,i+1,true);
        s[i]='0';
        s2[i]='1';
        generateInf(s,s2,i+1,false);
        s[i]='1';
        s2[i]='0';
        generateInf(s2,s,i+1,true);
        s[i]=s2[i]='?';
    }
    else if(s[i]=='?') {
        s[i] = s2[i];
        generateOne(s,s2,i+1);
        s[i]='9';
        generateInf(s,s2,i+1,false);
        s[i] = ((s2[i]-'0')-1+10)%10+'0';
        generateInf(s,s2,i+1,false);
        s[i]=((s2[i]-'0')+1)%10+'0';
        generateInf(s2,s,i+1,true);
        s[i]='0';
        generateInf(s2,s,i+1,true);
        s[i]='?';
    }
    else if(s2[i]=='?') {
        s2[i] = s[i];
        generateOne(s,s2,i+1);
        s2[i] = ((s[i]-'0')-1+10)%10+'0';

        generateInf(s2,s,i+1,true);
        s2[i]='9';
        generateInf(s2,s,i+1,true);
        s2[i]=((s[i]-'0')+1)%10+'0';
        generateInf(s,s2,i+1,false);
        s2[i]='0';
        generateInf(s,s2,i+1,false);
        s2[i]='?';
    }else {
        generateOne(s,s2,i+1);
    }
}

int main()
{

    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out


    int nbCas;
    cin>>nbCas;

    for(int c=1;c<=nbCas;c++) {
        cout<<"Case #"<<c<<": ";
        string s1,s2;
        cin>>s1>>s2;
        best = 1e19;


        generateOne(s1,s2,0);
        cout<<res1<<" "<<res2<<endl;
    }



}
