#include<iostream>
#include<iomanip>
#include<vector>
#include<iterator>
#include<algorithm>

using namespace std;

typedef vector<double> vi;
typedef vector<double>::iterator vii;
bool truth=false;

int ans[60][3],tc;

ostream_iterator<double> o(cout," ");

void rem(vi &v,double d)
{
	vii newEnd = remove(v.begin(),v.end(),d);
	v.erase(newEnd,v.end());
}

double mchoose(vi &vm,double kc)
{
	if(truth)
	{
		vii p;
		double mc=0;
		for(p=vm.begin();p!=vm.end();p++)
		{
			if(*p > kc )
			{
				mc=*p;
				rem(vm,mc);
				truth=false;
				return mc;
			}
		}
	}
	double mmin=1;
	vii p;
	for(p=vm.begin();p!=vm.end();p++)
	{
		if(*p < mmin)
		{
			mmin=*p;
		}
	}
	rem(vm,mmin);
	return mmin;
}

double mtell(vi &vm,vi &vk)
{
	double choice=0,mmax=0,mmin=1,kmax=0;
	vii p;
	for(p=vm.begin();p!=vm.end();p++)
	{
		if(*p > mmax)
		{
			mmax=*p;
		}
		if(*p < mmin)
		{
			mmin = *p;
		}
	}

	for(p=vk.begin();p!=vk.end();p++)
	{
		if(*p > kmax)
		{
			kmax=*p;
		}
	}
	
	if(vk.size() == 1)
	{
		choice = mmax;
	}
	else if(mmax > kmax)
	{
		truth=true;
		choice = mmax;
	}
	else
		choice = (*(vk.end()-2)) + 0.0000001;
	
	return choice;
}

double kchoose(vi &vk,double mc)
{
	double kc=0;
	vii p=vk.begin();
		
	for(p=vk.begin();p!=vk.end();p++)
	{
		if(*p>mc && kc==0)
		{
			kc=(*p);
			rem(vk,kc);
			return kc;
		}
	}
	
	kc=*(vk.begin());
	rem(vk,kc);
	return kc;
	
}

int main()
{
	cin>>tc;
	
	for(int z=0;z<tc;z++)
	{
		int n;
		double temp;
		cin>>n;
		vi vm,vk,vmb,vkb;
		vii p;
		
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			vm.insert(vm.end(),temp);
		}
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			vk.insert(vk.end(),temp);
		}
		
		sort(vm.begin(),vm.end());
		sort(vk.begin(),vk.end());
		
		for(p=vm.begin();p!=vm.end();p++)
		{
			vmb.insert(vmb.end(),*p);
		}
		for(p=vk.begin();p!=vk.end();p++)
		{
			vkb.insert(vkb.end(),*p);
		}
		
		cout.setf(ios::fixed,ios::floatfield);
		cout.setf(ios::showpoint);
		cout.precision(7);
		
		int war=0,dwar=0;
		
		while(vk.size()!=0)
		{
			double mt,kc,mc;
			mt = mtell(vm,vk);
			kc = kchoose(vk,mt);
			mc = mchoose(vm,kc);
			
			if(mc>kc)
				dwar++;
			
		//	cout<<"mt : "<<mt<<" | kc : "<<kc<<" | mc : "<<mc<<endl;
			
		
		/*	cout<<"vm ,vk :";
			copy(vm.begin(),vm.end(),o);
			cout<<endl;
			copy(vk.begin(),vk.end(),o);
			cout<<endl;
		*/	
		}
		
		//cout<<"\n\n\n";
		
		
		for(p=vmb.begin();p!=vmb.end();p++)
		{
			double mt,kc,mc;
			mc= (*p);
			kc=kchoose(vkb,mc);
			//c1out<<"mt : "<<mt<<" | kc : "<<kc<<" | mc : "<<mc<<endl;
			if(mc>kc)
				war++;
		}
		ans[z][0]=dwar;
		ans[z][1]=war;
		//cout<<"war : "<<war<<" dwar : "<<dwar;	
	}
	
	for(int z=0;z<tc;z++)
	{
		cout<<"Case #"<<z+1<<": "<<ans[z][0]<<" "<<ans[z][1]<<endl;
	}
	
	return 0;
}
