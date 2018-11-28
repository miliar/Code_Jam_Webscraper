#include <iostream>
#include <string>
#include <map>
using namespace std;

bool isgreater(int* a,int* b)
{
	if(a[0]<b[0])
		return false;
	if(a[0]>b[0])
		return true;
	if(a[1]>=b[1]-1)//nothing left for middle part
		return true;
	return false;
}

void createmap(map<char,map<char,string> > &multiply)
{
	multiply['1']['1']="+1";
	multiply['1']['i']="+i";
	multiply['1']['j']="+j";
	multiply['1']['k']="+k";
	multiply['i']['1']="+i";
	multiply['i']['i']="-1";
	multiply['i']['j']="+k";
	multiply['i']['k']="-j";
	multiply['j']['1']="+j";
	multiply['j']['i']="-k";
	multiply['j']['j']="-1";
	multiply['j']['k']="+i";
	multiply['k']['1']="+k";
	multiply['k']['i']="+j";
	multiply['k']['j']="-i";
	multiply['k']['k']="-1";
}

int main()
{
	int T,L,X,n=1;
	string input,prodstart,prodend,prodmiddle,prodmiddle1,prodmiddle2,prodmiddle3,prodline;
	map <char,map<char,string> > multiply;
	createmap(multiply);
	int iend[2],kstart[2];
	bool status,ans;
	cin>>T;
	while(n<=T)
	{
		prodstart="+1";
		prodend="+1";
		prodmiddle="+1";
		status = false;
		ans=true;
		cin>>L>>X;
		cin>>input;
		for(int x=0;x<X;x++)
		{
			for(int l=0;l<L;l++)
			{
				if(prodstart[0]=='+')
				{
					prodstart=multiply[prodstart[1]][input[l]];
				}
				else
				{
					prodstart=multiply[prodstart[1]][input[l]];
					prodstart[0]=(prodstart[0]=='+')?'-':'+';
				}
				if(prodstart=="+i")
				{
					iend[0]=x;
					iend[1]=l;
					status=true;
					break;
				}
			}
			if(status==true)
				break;
		}
		if(status==false)
		{
            ans=false;
		}
        if(ans==true)
        {
            status=false;
            for(int x=X-1;x>=iend[0];x--)
            {
                for(int l=L-1;l>=0;l--)
                {
                    if(prodend[0]=='+')
                    {
                        prodend=multiply[input[l]][prodend[1]];
                    }
                    else
                    {
                        prodend=multiply[input[l]][prodend[1]];
                        prodend[0]=(prodend[0]=='+')?'-':'+';
                    }
                    if(prodend=="+k")
                    {
                        kstart[0]=x;
                        kstart[1]=l;
                        status=true;
                        break;
                    }
                }
                if(status==true)
                    break;
            }
            if(status==false)
                ans=false;
        }
		if(isgreater(iend,kstart))
		{
			ans=false;
		}
		if(ans==true)
		{
			if(iend[0]==kstart[0])
			{
                for(int l=iend[1]+1;l<kstart[1];l++)
                {
                    if(prodmiddle[0]=='+')
                    {
                        prodmiddle=multiply[prodmiddle[1]][input[l]];
                    }
                    else
                    {
                        prodmiddle=multiply[prodmiddle[1]][input[l]];
                        prodmiddle[0]=(prodmiddle[0]=='+')?'-':'+';
                    }
                }
			}
			else
			{
                prodmiddle1="+1";
                prodmiddle2="+1";
                prodmiddle3="+1";
                for(int l=iend[1]+1;l<L;l++)
                {
                    if(prodmiddle1[0]=='+')
                    {
                        prodmiddle1=multiply[prodmiddle1[1]][input[l]];
                    }
                    else
                    {
                        prodmiddle1=multiply[prodmiddle1[1]][input[l]];
                        prodmiddle1[0]=(prodmiddle1[0]=='+')?'-':'+';
                    }
                }
                for(int l=0;l<kstart[1];l++)
                {
                    if(prodmiddle3[0]=='+')
                    {
                        prodmiddle3=multiply[prodmiddle3[1]][input[l]];
                    }
                    else
                    {
                        prodmiddle3=multiply[prodmiddle3[1]][input[l]];
                        prodmiddle3[0]=(prodmiddle3[0]=='+')?'-':'+';
                    }
                }
                if(iend[0]!=kstart[0]-1)
                {
                    prodline="+1";
                    for(int l=0;l<L;l++)
                    {
                        if(prodline[0]=='+')
                        {
                            prodline=multiply[prodline[1]][input[l]];
                        }
                        else
                        {
                            prodline=multiply[prodline[1]][input[l]];
                            prodline[0]=(prodline[0]=='+')?'-':'+';
                        }
                    }
                    for(int i=0;i<kstart[0]-iend[0]-1;i++)
                    {
                        if(prodmiddle2[0]=='+'&&prodline[0]=='+'||prodmiddle2[0]=='-'&&prodline[0]=='-')
                        {
                            prodmiddle2=multiply[prodmiddle2[1]][prodline[1]];
                        }
                        else
                        {
                            prodmiddle2=multiply[prodmiddle2[1]][prodline[1]];
                            prodmiddle2[0]=(prodmiddle2[0]=='+')?'-':'+';
                        }
                    }
                }
                if(prodmiddle1[0]=='+'&&prodmiddle2[0]=='+'||prodmiddle1[0]=='-'&&prodmiddle2[0]=='-')
                {
                    prodmiddle=multiply[prodmiddle1[1]][prodmiddle2[1]];
                }
                else
                {
                    prodmiddle=multiply[prodmiddle1[1]][prodmiddle2[1]];
                    prodmiddle[0]=(prodmiddle[0]=='+')?'-':'+';
                }
                if(prodmiddle[0]=='+'&&prodmiddle3[0]=='+'||prodmiddle[0]=='-'&&prodmiddle3[0]=='-')
                {
                    prodmiddle=multiply[prodmiddle[1]][prodmiddle3[1]];
                }
                else
                {
                    prodmiddle=multiply[prodmiddle[1]][prodmiddle3[1]];
                    prodmiddle[0]=(prodmiddle[0]=='+')?'-':'+';
                }
            }
			if(prodmiddle!="+j")
				ans=false;
		}
		cout<<"Case #"<<n<<": ";
		if(ans==true)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
		n++;
	}
	return 0;
}
