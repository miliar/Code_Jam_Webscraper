#include<iostream>
#include <algorithm>
#include<string>
using namespace std;

string findZero(string);

string findTwo(string);

string findEight(string);

string findSix(string);

string findThree(string);

string findSeven(string);

string findFive(string);

string findFour(string);

string findOne(string);

string findNine(string);

string output="";

int main(){
    int t;
    cin>>t;
    int x=1;
    while(x<=t){
        string o;
        string str;
        cin>>str;
        output="";
        str = findZero(str);
        str = findTwo(str);
        str = findSix(str);
        str = findEight(str);
        str = findThree(str);
        str = findSeven(str);
        str = findFive(str);
        str = findFour(str);
        str = findOne(str);
        str = findNine(str);
        sort(output.begin(), output.end());
        cout<<"Case #"<<x<<": "<<output<<endl;
        x++;
    }
}

string findNine(string str){
    int c=0;
    int tmpC=0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'N'){
            tmpC++;
        }
    }
    c = tmpC/2;
    if(c== 0){
        return str;
    }
     for(int i=0;i<c;i++){
        output = output+"9";
    }
    int j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'N'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'I'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'N'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    return str;
}

string findOne(string str){
    int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'N'){
            for(int j=0;j<str.length();j++){
                if(str[j] == 'O'){
                    str[j] = '0';
                    c++;
                }
            }
        }
    }
    int j=c;
    if(c== 0){
        return str;
    }
    for(int i=0;i<c;i++){
        output = output+"1";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'O'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'N'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    return str;
}

string findFive(string str){
    int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'V' || str[i]=='v'){
                c++;
        }
    }
    int j=c;
    if(c== 0){
        return str;
    }
    for(int i=0;i<c;i++){
        output = output+"5";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'F'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'I'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'V'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    return str;
}

string findFour(string str){
    int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'F' || str[i]=='f'){
                c++;
        }
    }
    int j=c;
    if(c== 0){
        return str;
    }
        for(int i=0;i<c;i++){
        output = output+"4";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'F'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'O'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'U'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'R'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    return str;
}

string findSeven(string str){
     int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'S' || str[i]=='s'){
                c++;
        }
    }
    int j=c;

    if(c== 0){
        return str;
    }
        for(int i=0;i<c;i++){
        output = output+"7";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'S'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'V'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'N'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    return str;
}

string findEight(string str){
    int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'G' || str[i]=='G'){
                c++;
        }
    }
    int j=c;
    if(c== 0){
        return str;
    }
        for(int i=0;i<c;i++){
        output = output+"8";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'I'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'G'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'H'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'T'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    return str;
}

string findThree(string str){
    int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'H' || str[i]=='h'){
                c++;
        }
    }
    int j=c;
    if(c== 0){
        return str;
    }
        for(int i=0;i<c;i++){
        output = output+"3";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'T'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'H'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'R'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    return str;
}

string findSix(string str){
    int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'X' || str[i]=='x'){
                c++;
        }
    }
    int j=c;
    if(c== 0){
        return str;
    }
        for(int i=0;i<c;i++){
        output = output+"6";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'X'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'S'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'I'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    return str;
}

string findTwo(string str){
    int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'W' || str[i]=='w'){
                c++;
        }
    }
    int j=c;
    if(c== 0){
        return str;
    }
        for(int i=0;i<c;i++){
        output = output+"2";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'W'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'T'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'O'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    return str;
}

string findZero(string str){
    int c = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'Z' || str[i]=='z'){
                c++;
        }
    }
    int j=c;
    if(c== 0){
        return str;
    }
        for(int i=0;i<c;i++){
        output = output+"0";
    }
    for(int i=0;i<str.length();i++){
        if(str[i] == 'Z'){
            str[i] ='0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'E'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }
    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'R'){
            str[i] = '0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    j=c;
    for(int i=0;i<str.length();i++){
        if(str[i] == 'O'){
            str[i] ='0';
            j--;
        }
        if(j==0){
            break;
        }
    }

    return str;
}
