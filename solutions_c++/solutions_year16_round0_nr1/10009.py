{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 // Example program\
#include <iostream>\
#include <string>\
#include <set>\
\
using namespace std;\
int main()\
\{\
    int t;\
    long long n;\
    cin>>t;\
    for(int i=1;i<=t;++i) \{\
        cin>>n;\
        set<long long>ss;\
        set<int> digits;\
        bool ok = 0;\
        long long last = 0;\
        for (int j=1;;j++) \{\
            long long m = n*j;\
            last = m;\
            if(!ss.insert(m).second) \{\
                break;\
            \}\
            while(m) \{\
                digits.insert(m%10);\
                m/=10;\
            \}\
            if(digits.size()==10) \{\
                ok = 1;\
                break;\
            \}\
                \
        \}\
        cout << "Case #"<<i<<": " ;\
        if (!ok) \
            cout <<"INSOMNIA"<<endl;\
        else\
            cout<< last<<endl;\
        \
    \}\
\}\
}