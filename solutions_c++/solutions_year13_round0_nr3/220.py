//
//  main.cpp
//  Google
//
//  Created by Mec0825 on 13-4-13.
//  Copyright (c) 2013年 Mec0825. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

//bool checkReverse(long long num) {
//    int numc[20],cnt=0;
//    while (num) {
//        numc[cnt++] = num%10;
//        num /= 10;
//    }
//    
//    bool success = 1;
//    for(int i = 0; i < cnt/2; i++) {
//        if(numc[i] != numc[cnt-i-1]) success = 0;
//    }
//    
//    return success;
//}

//long long numList[86] = {
//    1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 400000080000004, 10000000200000001, 10002000300020001, 10004000600040001, 10020210401202001, 10022212521222001, 10024214841242001, 10201020402010201, 10203040504030201, 10205060806050201, 10221432623412201, 10223454745432201, 12100002420000121, 12102202520220121, 12104402820440121, 12122232623222121, 12124434743442121, 12321024642012321, 12323244744232321, 12343456865434321, 12345678987654321, 40000000800000004, 40004000900040004, 1000000002000000001, 1000220014100220001, 1002003004003002001, 1002223236323222001, 1020100204020010201, 1020322416142230201, 1022123226223212201, 1022345658565432201, 1210000024200000121, 1210242036302420121, 1212203226223022121, 1212445458545442121, 1232100246420012321, 1232344458544432321, 1234323468643234321, 4000000008000000004
//};

vector<string> numList;

void dfs(int sum, int length, string str) {
    
    string nstr = str;
    reverse(nstr.begin(), nstr.end());
    
    if(length != 0) {
        string nstr1 = str + '0' + nstr;
        if(nstr1.length() <= 51 && sum*2 < 10) {
            numList.push_back(nstr1);
        }
        
        nstr1 = str + nstr;
        if(nstr1.length() <= 51 && sum*2 < 10) {
            numList.push_back(nstr1);
            
            dfs(sum, length+1, str + '0');
        }
        
    }
    
    string nstr1 = str + '1' + nstr;
    if(nstr1.length() <= 51 && sum*2+1 < 10) {
        numList.push_back(nstr1);
    }
    
    if(nstr1.length() <= 51 && sum*2 < 10) {
        
        dfs(sum+1, length+1, str + '1');
    }
    
    nstr1 = str + '2' + nstr;
    if(nstr1.length() <= 51 && sum*2+4 < 10) {
        numList.push_back(nstr1);
    }
    
    if(nstr1.length() <= 51 && sum*2 < 10) {
        
        dfs(sum+4, length+1, str + '2');
    }
    
    nstr1 = str + '3' + nstr;
    if(nstr1.length() <= 51 && sum*2+9 < 10) {
        numList.push_back(nstr1);
    }
    
    if(nstr1.length() <= 51 && sum*2 < 10) {
        
        dfs(sum+9, length+1, str + '3');
    }
}

int num[201];

string sqr(string str) {
    memset(num, 0, sizeof(num));
    
    for(int i = (int)str.size()-1; i >= 0; i--) {
        for(int j = (int)str.size()-1; j >= 0; j--) {
            num[(int)str.size()-1-i+(int)str.size()-1-j] += (str[i]-'0')*(str[j]-'0');
        }
    }
    
    for(int i = 0; i < 200; i++) {
        num[i+1] += num[i] / 10;
        num[i] %= 10;
    }
    
    int p = 200;
    for(p = 200; p >= 0; p--) {
        if(num[p] != 0) break;
    }
    
    string res = "";
    for(int i = p; i >= 0; i--) {
        res += '0'+num[i];
    }
    
    return res;
}

bool cmp(string a,string b)
{
    if(a.length() == b.length()) {
        return a < b;
    }
    return a.length() < b.length();
}

int pos(string a) {
    int l, r, mid;
    l = 0; r = (int)numList.size();
    
    while (l < r) {
        mid = (l + r) / 2;
        
        if(!cmp(numList[mid], a)){
            r = mid;
        }
        else {
            l = mid + 1;
        }
    }
    
    return r;
}

int main()
{
    freopen("/Users/Mec0825/Documents/Google/2013/Qualification/C-in.txt", "r", stdin);
    freopen("/Users/Mec0825/Documents/Google/2013/Qualification/C-out.txt", "w", stdout);
    
//    vector<long long> res;
//    
//    for(int i = 1; i <= 100000; i++) {
//        long long reverse = 0;
//        long long num = i;
//        long long pow = 1;
//        while (num) {
//            
//            reverse = reverse*10+num%10;
//            pow *= 10;
//            
//            num /= 10;
//        }
//        
//        if(checkReverse(((i/10*pow)+reverse)*((i/10*pow)+reverse))) {
//            res.push_back(((i/10*pow)+reverse)*((i/10*pow)+reverse));
//        }
//        
//        if(checkReverse((i*pow+reverse)*(i*pow+reverse))) {
//            res.push_back((i*pow+reverse)*(i*pow+reverse));
//        }
//        
//    }
//    
//    sort(res.begin(),res.end());
//    
//    for(int i = 0; i < res.size(); i++) {
//        printf("%lld, ",res[i]);
//    }
    
//    int numc;
//    
//    scanf("%d", &numc);
//    
//    for(int t = 0; t < numc; t++) {
//        long long a, b;
//        scanf("%lld %lld", &a, &b);
//    
//        int st, ls;
//        
//        for(st = 0; st < 86; st++) {
//            if(a <= numList[st]) break;
//        }
//        
//        for(ls = 85; ls >= 0; ls--) {
//            if(b >= numList[ls]) break;
//        }
//        
//        printf("Case #%d: %d\n",t+1,ls-st+1);
//    }
    
    dfs(0,0,"");
    
    sort(numList.begin(), numList.end(),cmp);
    
    for(int i = 0; i < numList.size(); i++) {
        numList[i] = sqr(numList[i]);
    }
    
    int numc;
    
    scanf("%d", &numc);
    
    for(int t = 0; t < numc; t++) {
        string a, b;
        cin >> a >> b;
        
        int posb, posa;
        posa = pos(a);
        posb = pos(b);
        int res = posb-posa+1;
        
        if(b != numList[posb]) res--;
        
        printf("Case #%d: %d\n",t+1,res);
    }
    
//    for(int i = 0; i < 100; i++) {
//        printf("%s\n", numList[i].c_str());
//    }
//    
//    printf("%d\n",(int)numList.size());
    
    return 0;
}
