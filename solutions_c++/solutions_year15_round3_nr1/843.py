
int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin>>t;
    for(int cases=1;cases<=t;cases++)
        {
        int r,c,w;
        cin>>r>>c>>w;
        if(r==1)
           { if(c%w==0)
		result=c/w+(w-1);
	       else
		result=c/w+w;
           }
        else
            {
            result=(c/w)*(r-1);
            if(c%w==0)
		result+=(c/w+(w-1));
	       else
		result+=(c/w+w);
        }
        cout<<"Case #"<<cases<<": "<<result<<"\n";

    }


    return 0;
}