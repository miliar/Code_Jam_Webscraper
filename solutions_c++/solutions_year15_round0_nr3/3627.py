#include <iostream>
#include <cstdio>

using namespace std;

int a[][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

int opfind(char a)
{
	if(a=='1')
	return 1;
	if(a=='i')
	return 2;
	if(a=='j')
	return 3;
	if(a=='k')
	return 4;
}

int mod(int a)
{
	if(a<0)
	return -a;
	else return a;
}

int op(int op1, int op2)
{
	int ans=a[mod(op1)-1][mod(op2)-1];
	if(op1*op2<0)
	return -ans;
	else
	return ans;
}

int inv_op(int op1,int op2)
{
	int i,sg,ans;
	if(op1>=0)
	sg=1;
	else
	sg=-1;
	for(i=0;i<4;i++)
	{
		if(a[mod(op1)-1][i]==op2)
		ans=i+1;
		else if(a[mod(op1)-1][i]==-op2)
		ans=-i-1;
	}
	return sg*ans;
}

int main()
{
	freopen("C-small-attempt4.in","r",stdin);
	freopen("out1.txt","w",stdout);
	int t,j,l,i,z,prev,pos_i,pos_j,pos_k,arr[1000000],arr2[1000000],req_op,next_pos_i,next_pos_j,next_pos_k,start_j,start_k,r1,r2,op1,op2,opp,opp2;
	long long int x,remaining;
	string str;
	//cout << op(4,4) << endl;
	cin >> t;
	for(z=1;z<=t;z++)
	{
		cout << "Case #" << z << ": ";
		cin >> l >> x;
		remaining=l*x;
		cin >> str;
		//cout << "XXX\n";
		prev=1;
		pos_i=0;
		//cout << str << endl;
		//bool flag_i=true;
		for(i=0;i<l;i++)
		{
			//cout << opfind(str[i]) << endl;
			arr[i]=op(prev,opfind(str[i]));
			//cout << arr[i] << endl;
			prev=arr[i];
			if(arr[i]==2 && pos_i==0)
			{
				pos_i=i+1;
			}
		}
		opp=op(arr[l-1],arr[l-1]);
		opp2=op(opp,arr[l-1]);
		//cout << pos_i << endl;
		if(pos_i==0)
		{
			req_op=inv_op(arr[l-1],2);
			//cout << req_op << endl;
			next_pos_i=0;
			for(i=0;i<l;i++)
			{
				if(arr[i]==req_op)
				{
					next_pos_i=i+1;
					break;
				}
				else if(op(arr[l-1],arr[i])==req_op)
				{
					next_pos_i=i+l+1;
				}
				else if(op(opp,arr[i])==req_op)
				{
					next_pos_i=i+2*l+1;
				}
				else if(op(opp2,arr[i])==req_op)
				{
					next_pos_i=i+3*l+1;
				}
			}
			//cout << next_pos_i << endl;
			if(next_pos_i==0)
			{
				cout << "NO\n";
				continue;
			}
			else
			{
				pos_i=l+next_pos_i;
			}
		}
		//cout << pos_i << endl;
		remaining=remaining-pos_i;
		if(remaining<0)
		{
			cout << "NO\n";
			continue;
		}
		start_j=pos_i%l;
		//cout << start_j << endl;
		prev=1;
		pos_j=0;
		for(i=start_j;i<l;i++)
		{
			arr2[i]=op(prev,opfind(str[i]));
			prev=arr2[i];
			if(arr2[i]==3 && pos_j==0)
			pos_j=i+1-start_j;
		}
		//cout << pos_j << endl;
		if(pos_j==0)
		{
			req_op=inv_op(arr2[l-1],3);
			//cout << req_op << endl;
			next_pos_j=0;
			for(i=0;i<l;i++)
			{
				if(arr[i]==req_op)
				{
					next_pos_j=i+1;
					break;
				}
				else if(op(arr[l-1],arr[i])==req_op)
				{
					next_pos_j=i+l+1;
				}
				else if(op(opp,arr[i])==req_op)
				{
					next_pos_j=i+2*l+1;
				}
				else if(op(opp2,arr[i])==req_op)
				{
					next_pos_j=i+3*l+1;
				}
			}
			if(next_pos_j==0)
			{
				cout << "NO" << endl;
				continue;
			}
			else
			{
				pos_j=next_pos_j+l-start_j;
			}
		}
		//cout << pos_j << endl;
		remaining-=pos_j;
		if(remaining<0)
		{
			cout << "NO\n";
			continue;
		}
		/*start_k=(pos_i+pos_j)%l;
		//cout << start_k << endl;
		prev=1;
		pos_k=0;
		for(i=start_k;i<l;i++)
		{
			arr2[i]=op(prev,opfind(str[i]));
			prev=arr2[i];
			if(arr2[i]==4)
			pos_k=i+1-start_k;
		}
		//cout << arr2[l-1] << endl;
		if(pos_k==0)
		{
			req_op=inv_op(arr2[l-1],4);
			//cout << req_op << endl;
			next_pos_k=0;
			for(i=0;i<l;i++)
			{
				if(arr[i]==req_op)
				{
					next_pos_k=i+1;
					break;
				}
			}
			if(next_pos_k==0)
			{
				cout << "NO\n";
				continue;
			}
			else
			{
				pos_k=next_pos_k+l-start_k+1;
			}
		}
		remaining-=pos_k;
		if(remaining<0)
		{
			cout<< "NO\n";
			continue;
		}*/
		r1=remaining%l;
		//cout << remaining << " " << r1 << endl;
		op1=1;
		for(i=1;i<=r1;i++)
		{
			op1=op(opfind(str[l-i]),op1);
		}
		//cout << op1 << endl;
		r2=remaining/l;
		op2=1;
		for(i=1;i<=r2;i++)
		{
			op2=op(op2,arr[l-1]);
		}
		op2=op(op1,op2);
		if(op2==4)
		cout << "YES\n";
		else
		cout << "NO\n";
	}
	return 0;
}
