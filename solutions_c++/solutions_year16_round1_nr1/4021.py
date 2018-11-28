#include<bits/stdc++.h>
using namespace std;
struct node
{
    char ch;
    node *lt;
};
void display(node *p)
{
    while(p!=NULL){
        cout<<(p->ch);
        p=p->lt;
    }
}
int main()
{
    freopen("A2.txt","r",stdin);
    freopen("out_A2.txt","w",stdout);
    int t,c,i,n;
    string S;
    cin>>t;
    node *p,*q,*root;
    for(c=1;c<=t;c++)
    {
        cin>>S;
        n=S.size();
        root=new node();
        root->ch=S[0];
        root->lt=NULL;
        q=root;
        for(i=1;i<n;i++){
            p=new node;
            p->ch=S[i];
            p->lt=NULL;
            if(S[i]<(root->ch))
            {
                q->lt=p;
                q=q->lt;
            }
            else{
                p->lt=root;
                root=p;
            }
        }
        cout<<"Case #"<<c<<": ";
        display(root);
        cout<<endl;
        delete(root);
        delete(p);
    }
return 0;
}
