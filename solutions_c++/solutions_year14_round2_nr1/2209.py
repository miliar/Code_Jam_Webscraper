#include<iostream>
#include<cstring>

using namespace std;
char strings[100][101];
int cnt[100];
int pos[100];


void do_a_case()
{
    int N;
    int eof=0;
    int distance=0;
    cin>>N;
    for(int i=0; i<N; ++i)
    {
        cin>>strings[i];
        pos[i]=cnt[i]=0;
        //cout<<strings[i]<<endl;
    }
    char lookup=strings[0][strlen(strings[0])-1];
    for(int i=0;i<N;++i)
    if(strings[i][strlen(strings[i])-1]!=lookup)
    {
        cout<<"Fegla Won\n";
                return;
    }

    while(!eof)
    {
        int i=0;
        char lookup=strings[0][pos[i]];
        for(; i<N; ++i)
        {
            cnt[i]=0;
            while(strings[i][pos[i]]==lookup)pos[i]++,cnt[i]++;
            if(cnt[i]==0)
            {
                cout<<"Fegla Won\n";
                return;
            }
            if(strings[i][pos[i]]=='\0')eof=1;
            if(eof)
                if(strings[i][pos[i]]!='\0')
                {
                    cout<<"Fegla Won\n";
                    return;
                }
                //cout<<cnt[i]<<" ";
        }
        int min=cnt[0],max=cnt[0];
        for(i=0; i<N; ++i)
        {
            if(cnt[i]>max)max=cnt[i];
            if(cnt[i]<min)min=cnt[i];
        }
        //cout<<endl<<max<<" "<<min<<endl;
        distance+=(max-min);
    }
    cout<<distance<<endl;

}

int main()
{
    int T;
    cin>>T;
    for(int i=0; i<T; ++i)
        {
            cout<<"Case #"<<i+1<<": ";
            //cout<<endl;
            do_a_case();}
    return 0;
}
