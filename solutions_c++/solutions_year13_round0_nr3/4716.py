
package problemacm;

import java.util.Scanner;
import java.math.BigInteger;
import java.util.ArrayList;


public class Main
{
        static boolean esPalindrome(BigInteger a)
        {
            String a1 = a.toString();
            for(int i=0; i<a1.length()/2; i++)
            {
                if(a1.charAt(i)!=a1.charAt(a1.length()-i-1)) return false;
            }

            return true;
        }



	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		ArrayList<BigInteger> resp = new ArrayList <BigInteger> ();
                BigInteger diez = new BigInteger("10");
                BigInteger tope = (diez.pow(7)).add(BigInteger.ONE);
                
                for(BigInteger a = new BigInteger("1"); a.compareTo(tope)<0; a=a.add(BigInteger.ONE))
                {
                    if(esPalindrome(a) && esPalindrome(a.pow(2)))
                    {
                        resp.add(a.pow(2));
                        //System.out.println(a.pow(2));
                    }
                }

                int t = in.nextInt();
                BigInteger desde = new BigInteger("0");
                BigInteger hasta = new BigInteger("0");
                //BigInteger a = new BigInteger("0");
                //BigInteger b = new BigInteger("0");
                int cont=-1;
                for(int i=1; i<=t; i++)
                {
                    desde=in.nextBigInteger();
                    hasta=in.nextBigInteger();
                    cont =0;

                    for(int ii=0; ii<resp.size(); ii++)
                    {
                        if(resp.get(ii).compareTo(desde)>=0 && resp.get(ii).compareTo(hasta)<=0)
                            cont++;
                    }

                    System.out.println("Case #"+i+": "+cont);
                }

                
	}
}

