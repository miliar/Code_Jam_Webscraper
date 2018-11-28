#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int main() {

	int T,N,i,q,ctr=0;
	char S[101];

	cin>>T;

	int w=1;
	while(w<=T)
	{
	    ctr=0;
	    cin>>S;
	    //len=strlen(S);
/*
        for(q=0;q<len;++q);
        {
            R[q]='+';
        }

        R[len]='\0';
        cout<<" "<<R;
        //strcpy(R,"++++");
        while(strcmp(S,R)!=0)
*/      while(1)
        {
            int j,k,p;
            char temp;

            //cout<<" S:"<<S;
            //getchar();
            for(j=0;S[0]==S[j];++j);
            if(S[j]=='\0')
            {
                //cout<<" ALL SAME ";
                if(S[0]=='-')
                {
                    ctr++;
                }
                break;
            }
            else
            {
                //cout<<" Swaping";
                for(k=0,p=j-1;k<=p;k++,p--)
                {
                    if(k==p){
                        S[k]=(S[k]=='+')?'-':'+';//cout<<" S_I_i1:"<<S;
                        }
                    else{
                        temp=(S[k]=='+')?'-':'+';//cout<<" S_I_e1:"<<S;
                        S[k]=(S[p]=='+')?'-':'+';//cout<<" S_I_e2:"<<S;
                        S[p]=temp;//cout<<" S_I_e3:"<<S;
                    }
                }
                ctr++;
            }
        }
        //cout<<"\nCTR = "<<ctr;
        cout<<"Case #"<<w<<": "<<ctr<<endl;
        w++;

	}

	return 0;
}
