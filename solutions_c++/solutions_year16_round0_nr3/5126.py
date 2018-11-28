/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.BigInteger;
import java.lang.Math.*;
import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	static char x[]=new char[16];
	static BigInteger divs[]=new BigInteger[11];
	static BigDecimal sqrt(BigInteger num)
	{
	String n = "";
                   
                MathContext mc =  new MathContext(0, RoundingMode.DOWN);
                mc = MathContext.DECIMAL32;
 
                BigInteger my2P100000  = num;
                BigInteger two      = new BigInteger("2");
                BigInteger one      = new BigInteger("1");
               
                //my2P100000  = two.shiftLeft(2000 - 1);
                       
                // System.out.println("2^2000 --  Step 1");
                // System.out.println("Value of 2^2,000 " + my2P100000  );
                // System.out.println("");
                // System.out.println("Finding the Square Root of 2^2000");
                               
               
                String mys =  my2P100000  + "";
                n = (mys) ;
                int firsttime = 0;
               
                BigDecimal myNumber = new BigDecimal(n);
                BigDecimal g = new BigDecimal("1");
                BigDecimal my2 = new BigDecimal("2");
                BigDecimal epsilon = new BigDecimal("0.0000000001");
       
                BigDecimal nByg = myNumber.divide(g, 9, BigDecimal.ROUND_FLOOR);
               
                //Get the value of n/g
                BigDecimal nBygPlusg = nByg.add(g);
               
                //Get the value of "n/g + g
                BigDecimal nBygPlusgHalf =  nBygPlusg.divide(my2, 9, BigDecimal.ROUND_FLOOR);
               
                //Get the value of (n/g + g)/2
                BigDecimal  saveg = nBygPlusgHalf;
                firsttime = 99;
               
                do
                {
                        g = nBygPlusgHalf;
                        nByg = myNumber.divide(g, 9, BigDecimal.ROUND_FLOOR);
                        nBygPlusg = nByg.add(g);
                        nBygPlusgHalf =  nBygPlusg.divide(my2, 9, BigDecimal.ROUND_FLOOR);
                        BigDecimal  savegdiff  = saveg.subtract(nBygPlusgHalf);
                           
                        if (savegdiff.compareTo(epsilon) == -1 )
                        {
                            firsttime = 0;
                        }
                        else
                        {
                            saveg = nBygPlusgHalf;
                        }
                       
                } while (firsttime > 1);
               
               // System.out.println("\nThe Square Root is " + saveg);
               return saveg;
	}
	
	static int prime(BigInteger num,int base)
	{
		//System.out.println("prime("+num.toString()+","+base+")");
		BigInteger div=new BigInteger("1");
		BigInteger i=new BigInteger("2");
		BigInteger lim=new BigInteger("0");
		int ret_value=0;
		lim=sqrt(num).toBigInteger();
		
		if(num.isProbablePrime(1)==false)
		{
		for(;i.compareTo(lim)==-1;i=i.add(BigInteger.ONE))
		{
			//if(base==9)
			//System.out.println("dsfadsf"+i.toString());
			if((num.mod(i)).toString()=="0")
			{
				ret_value=1;
				divs[base]=i;
				break;
			}
		}
		}
	//	System.out.println("ret="+ret_value);
		return ret_value;
	}
	static int check(int base)
	{
		//System.out.println("check("+base+")");
		BigInteger num=new BigInteger("0");
		BigInteger temp=new BigInteger(""+base);
		String te;
		for(int i=15,j=0;i>=0;i--,j++)
		{
			if(x[i]=='1')
			{
				//System.out.println("safdsadf");
			//temp=new BigInteger(""+Math.pow(base,j));
			
			//temp=(int)Math.pow(base,j);
			//te=""+temp;
			//System.out.println(te);
			num=num.add(temp.pow(j));
			//System.out.println(num.toString());
			}
		}
		int ch_prime=prime(num,base);
		return ch_prime;
	}
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		System.out.println("Case #1:");
		int k,j,ch,count_nums=0;
		x[0]='1';
		x[15]='1';
		for(int i=1;i<15;i++)
		{
			x[i]='0';
		}
		for(;count_nums<50;)
		{
			x[14]++;
			if(x[14]=='2')
			{
				x[14]='0';
				
				for(k=13;x[k]!='0'&&k>=0;k--)
				{
			//	System.out.println("for(k=13;"+x[k]+"!=0&&"+k+">=0;"+k+"--)");
				
				x[k]='0';
				}
				if(k==-1)
				break;
				x[k]='1';
			}
			/*for(int i=0;i<16;i++)
				{
					System.out.print(x[i]);
				}
				System.out.println();*/
			for(j=2;j<=10;j++)
			{
				ch=check(j);
				if(ch==0)
				break;
			}
			
			if(j==11)
			{
				count_nums++;
				for(int i=0;i<16;i++)
				{
					System.out.print(x[i]);
				}
				System.out.print(" ");
				for(j=2;j<=10;j++)
				{
					//print the divisor
					System.out.print(divs[j].toString()+" ");
				}
				System.out.println();
			}
		
		}
	}
}