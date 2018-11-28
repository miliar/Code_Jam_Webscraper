//
//  main.cpp
//  codejam
//
//  Created by Christiana on 16/4/9.
//  Copyright © 2016年 Christiana. All rights reserved.
//


#include <iostream>
#include <ext/hash_set>
#include <fstream>
#include <cstring>

using namespace std;
using namespace __gnu_cxx;

hash_set<int> getNum(int n){
    hash_set<int> hash;
    while(n!=0){
        hash.insert(n % 10);
        n = n / 10;
    }
    return hash;
}

void CountSheep(){
    //freopen("./A-small-attempt0.in","r",stdin);
    //freopen("./out.txt", "w", stdout);
    ifstream fin;
    ofstream fout;
    fin.open("/Users/christiana/Documents/workspace/leetcode/codejam/codejam/A-large.in");
    fout.open("/Users/christiana/Documents/workspace/leetcode/codejam/codejam/output-large.txt");
    int n;
    //cin >> n;
    fin>>n;
    int todo;
    for(int i = 0; i < n; ++i){
        //cin >> todo;
        fin >> todo;
        hash_set<int> count;
        if(todo == 0){
            //cout << "Case #" << i+1 << ": INSOMINIA"<< endl;
            fout << "Case #" << i+1 << ": INSOMNIA"<< endl;
            continue;
        }
        else{
            int k = 1;
            while(count.size()!=10){
                count.insert(getNum(todo*k).begin(),getNum(todo*k).end());
                k++;
            }
            //cout << "Case #" << i+1 << ": " << (k-1)*todo << endl;
            fout << "Case #" << i+1 << ": " << (k-1)*todo << endl;
        
        }
        
    }
}

void shiyan(){
    
    string news = "-+-+-+-+";
    for(int i = 0; i < news.size(); ++i){
        if(news[i] == '-'){
            news[i] = '+';
        }
        else{
            news[i] = '-';
        }
    }
    cout <<news << endl;
}

int countPancake(string st){
    bool flag = true;
    for(int j = st.size() - 1; j >= 0; --j){
        if(st[j] == '+'){
            
            cout << "continue" << endl;
            continue;
        }
        else{
            flag = false;
        }
    }
    if(flag){
        return 0;
    }
    
    flag = true;
    for(int j = st.size() - 1; j >= 0; --j){
        if(st[j] == '-'){
            
            cout << "continue" << endl;
            continue;
        }
        else{
            flag = false;
        }
    }
    if(flag){
        return 1;
    }

    
    if(st == "-"){
        return 1;
    }
    if(st.size() == 0){
        return 0;
    }
    
    int min = 10000;
    
    //翻最上面i个
    for(int i = 1; i <= st.size(); ++i){
        //cout << st << endl;
        string top1 = st.substr(0, i);
        //cout << "top1" << top1;
        string bottom = st.substr(i, st.size());
        //cout << "bottom" << bottom << endl;
        reverse(top1.begin(), top1.end());
        //翻？
        for(int j = 0; j < top1.size(); j++){
            if(top1[j] == '-'){
                top1[j] = '+';
            }
            else{
                top1[j] = '-';
            }
        }
        string newst(top1 + bottom);
        cout << "newst" << newst << endl;
        if(newst == st){
            cout << "same" << endl;
            continue;
        }
        //递归
        flag = true;
        for(int j = newst.size() - 1; j >= 0; --j){
            cout << newst[j] << endl;
            if(newst[j] == '+'){
                
                cout << "continue" << endl;
                continue;
            }
            else{
                flag = false;
                string subset = newst.substr(0,j+1);
                cout << "subset"<< subset << endl;
                if(countPancake(subset) < min){
                    min = countPancake(subset);
                }
                break;
            }
        }
        if(flag){
            min = 0;
        }
        //*/
    }
    return 1 + min;
}


int countPancake2(string st){
    bool flag = true;
    for(int j = st.size() - 1; j >= 0; --j){
        if(st[j] == '+'){
            
            //cout << "continue" << endl;
            continue;
        }
        else{
            flag = false;
            break;
        }
    }
    if(flag){
        return 0;
    }

    
    flag = true;
    for(int j = st.size() - 1; j >= 0; --j){
        if(st[j] == '-'){
            
            //cout << "continue" << endl;
            continue;
        }
        else{
            flag = false;
            break;
        }
    }
    if(flag){
        return 1;
    }
    
    for(int i = 1; i < st.size(); ++i){
        if(st[i] != st[i-1]){
            //翻
            string top1 = st.substr(0, i);
            //cout << "top1" << top1;
            string bottom = st.substr(i, st.size());
            //cout << "bottom" << bottom << endl;
            reverse(top1.begin(), top1.end());
            //翻？
            for(int j = 0; j < top1.size(); j++){
                if(top1[j] == '-'){
                    top1[j] = '+';
                }
                else{
                    top1[j] = '-';
                }
            }
            string newst(top1 + bottom);
            //cout << "newst" << newst << endl;
            return 1 + countPancake2(newst);
            break;
        }
        else
            continue;
    }
    
    return 0;
}

void pancake(){
    ifstream fin;
    ofstream fout;
    fin.open("/Users/christiana/Documents/workspace/leetcode/codejam/codejam/B-large.in");
    fout.open("/Users/christiana/Documents/workspace/leetcode/codejam/codejam/output-B-large.txt");
    int n;
    //cin>>n;
    fin>>n;
    for(int i = 0; i < n; ++i){
        string todo;
        //cin>>todo;
        fin>>todo;
        fout << "Case #" << i+1 << ": " <<countPancake2(todo) << endl;
        
    }
}


int main(int argc, const char * argv[]) {
    // insert code here...
    //CountSheep();
    pancake();
    //shiyan();
    
    return 0;
}
