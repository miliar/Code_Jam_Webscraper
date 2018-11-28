# include <bits/stdc++.h>
using namespace std;
int main()
{
    FILE *fp, *fq;
    fp=fopen("input.txt","rt");
    fq=fopen("output.txt","wt");
	int t;
	fscanf(fp,"%d",&t);
	int l=1;
	char s[102];
	while(t--)
	{
		fscanf(fp,"%s",&s);
		//printf("%s\n",s);
		long long count=0;
		int current=strlen(s)-1;
		//cout<<current<<endl;
		while(current!=0)
		{
			while(s[current]!='-' && current>0)
				current--;
            //cout<<current<<endl;
            if(current==0)
                break;
			int i=0;
			if(s[i]=='+')
			{
				count++;
				while(s[i]=='+')
				{
					s[i]='-';
					i++;
				}
			}
			//cout<<count<<endl;
			int flag=0;
			int mid=current/2;
			if(current%2!=1)
			{
				if(s[mid]=='+')
					s[mid]='-';
				else
					s[mid]='+';
                flag=1;
			}
			count++;
			//cout<<count<<endl;
			//break;
			if(flag==0)
                mid++;
			for(int j=0;j<mid;j++)
			{
				if(s[j]==s[current-j])
				{
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
					s[current-j]=s[j];
				}

			}
		}
		if(s[0]!='+')
		    count++;
		fprintf(fq,"Case #%d: %lld\n", l, count);
		l++;
	}
	return 0;
}