#include <bits/stdc++.h>

using namespace std;

bool verify (string stack){
    for (int i=0; i<stack.size(); i++){
        if (stack[i]=='-'){
            return false;
        }
    }
    return true;
}

void flip (string & stack, int in, int end){
    char temp, temp2;
    //cout<<"i: "<<in<<" e: "<<end<<endl;
    int tam = ((end+1)/2);
    for (int i=0; i<tam; i++){
        //cout<<" n: "<<i<<" m: "<<end-i<<endl;
        temp = stack[i];
        temp2 = stack[end-i];

        if (temp=='+')temp='-';
        else temp='+';

        if (temp2=='-')temp2='+';
        else temp2='-';
        //cout<<temp2<<"  "<<temp<<endl;
        stack[i] = temp2;
        stack[end-i] = temp;
        //cout<<stack<<endl;
    }
    if ((end+1)%2!=0){
        temp = stack[tam];
        if (temp=='+')temp='-';
        else temp='+';
        stack[tam] = temp;
    }
}

int main(){
    ifstream cin("B-large.in");
    ofstream cout("salbig.txt");
    int c, resp, j;
    string stack;
    cin>>c;
    for (int i=1; i<=c; i++){
        resp = 0;
        cin>>stack;
        for (j=stack.size()-1; j>=0; j-- ){
            if (stack[j]=='-')break;
        }
        bool finished = false;
        finished = verify(stack);
        while (!finished){
            int k=0;
            while (stack[k]=='+' && k<=j)k++;
            //cout<<"K: "<<k<<endl;
            flip(stack,0,k-1);
            if (k>0)resp++;
            //cout<<"s: "<<stack<<" "<<resp<<endl;
            if (verify(stack))break;
            while (stack[k]=='-' && k<=j)k++;
            //cout<<"J: "<<k<<endl;
            flip(stack,0,j);
            if (k>0)resp++;
            //cout<<"s: "<<stack<<" "<<resp<<endl;
            if (verify(stack))break;
            j -=k;
            //system("pause");
        }
        cout<<"Case #"<<i<<": "<<resp<<endl;
    }

    return 0;
}
