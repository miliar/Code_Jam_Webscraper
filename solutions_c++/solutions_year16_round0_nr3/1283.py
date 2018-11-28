#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int c=0,inp1,inp2;
	char s1[2],s2[2],s3[2],s4[2],s5[2],s6[2],s7[2],s8[2],s9[2];
	cin>>inp1;
    cout<<"Case #1:"<<endl;
	cin>>inp1>>inp2;
	if(inp1==16)
    for(int i1=0;i1<2;i1++)
    {
        if(i1)
            {s1[0]='1';s1[1]='1';}
        else
                {s1[0]='0';s1[1]='0';}
        for(int i1=0;i1<2;i1++)
        {
            if(i1)
                {s2[0]='1';s2[1]='1';}
            else
                {s2[0]='0';s2[1]='0';}
            for(int i1=0;i1<2;i1++)
            {
                if(i1)
                    {s3[0]='1';s3[1]='1';}
                else
                    {s3[0]='0';s3[1]='0';}
                for(int i1=0;i1<2;i1++)
                {
                    if(i1)
                        {s4[0]='1';s4[1]='1';}
                    else
                        {s4[0]='0';s4[1]='0';}
                    for(int i1=0;i1<2;i1++)
                    {
                        if(i1)
                            {s5[0]='1';s5[1]='1';}
                        else
                            {s5[0]='0';s5[1]='0';}
                        for(int i1=0;i1<2;i1++)
                        {
                            c++;
                            cout<<"11"<<s1[0]<<s1[1]<<s2[0]<<s2[1]<<s3[0]<<s3[1]<<s4[0]<<s4[1]<<s5[0]<<s5[1];
                            if(i1)
                                cout<<"11";
                            else
                                cout<<"00";
                            cout<<"11 3 4 5 6 7 8 9 10 11"<<endl;
                            
                            if(c==inp2)
                                return 0;
                        }
                    }
                }
            }
        }
    }
    else
    for(int i1=0;i1<2;i1++)
    {
        if(i1)
            {s1[0]='1';s1[1]='1';}
        else
                {s1[0]='0';s1[1]='0';}
        for(int i1=0;i1<2;i1++)
        {
            if(i1)
                {s2[0]='1';s2[1]='1';}
            else
                {s2[0]='0';s2[1]='0';}
            for(int i1=0;i1<2;i1++)
            {
                if(i1)
                    {s3[0]='1';s3[1]='1';}
                else
                    {s3[0]='0';s3[1]='0';}
                for(int i1=0;i1<2;i1++)
                {
                    if(i1)
                        {s4[0]='1';s4[1]='1';}
                    else
                        {s4[0]='0';s4[1]='0';}
                    for(int i1=0;i1<2;i1++)
                    {
                        if(i1)
                            {s5[0]='1';s5[1]='1';}
                        else
                            {s5[0]='0';s5[1]='0';}
                        for(int i1=0;i1<2;i1++)
                        {
                            if(i1)
                                {s6[0]='1';s6[1]='1';}
                            else
                                {s6[0]='0';s6[1]='0';}
                            for(int i1=0;i1<2;i1++)
                            {
                                if(i1)
                                    {s7[0]='1';s7[1]='1';}
                                else
                                    {s7[0]='0';s7[1]='0';}
                                for(int i1=0;i1<2;i1++)
                                {
                                    if(i1)
                                        {s8[0]='1';s8[1]='1';}
                                    else
                                        {s8[0]='0';s8[1]='0';}
                                    for(int i1=0;i1<2;i1++)
                                    {
                                        c++;
                                        cout<<"11"<<s1[0]<<s1[1]<<s2[0]<<s2[1]<<s3[0]<<s3[1]<<s4[0]<<s4[1]<<s5[0]<<s5[1]<<s6[0]<<s6[1]<<s7[0]<<s7[1]<<s8[0]<<s8[1];
                                        if(i1)
                                            cout<<"11";
                                        else
                                            cout<<"00";
                                        cout<<"0000000000";
                                        cout<<"11 3 4 5 6 7 8 9 10 11"<<endl;
                                        
                                        if(c==inp2)
                                            return 0;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
	return 0;
}

